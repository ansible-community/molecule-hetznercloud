import os

from molecule import logger, util
from molecule.api import Driver
from molecule.util import lru_cache, sysexit_with_message

log = logger.get_logger(__name__)


class HetznerCloud(Driver):
    def __init__(self, config=None):
        super(HetznerCloud, self).__init__(config)
        self._name = "hetznercloud"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login_cmd_template(self):
        connection_options = " ".join(self.ssh_connection_options)

        return (
            "ssh {{address}} "
            "-l {{user}} "
            "-p {{port}} "
            "-i {{identity_file}} "
            "{}"
        ).format(connection_options)

    @property
    def default_safe_files(self):
        return [self.instance_config]

    @property
    def default_ssh_connection_options(self):
        return self._get_ssh_connection_options()

    def login_options(self, instance_name):
        d = {"instance": instance_name}

        return util.merge_dicts(d, self._get_instance_config(instance_name))

    def ansible_connection_options(self, instance_name):
        try:
            d = self._get_instance_config(instance_name)

            return {
                "ansible_user": d["user"],
                "ansible_host": d["address"],
                "ansible_port": d["port"],
                "ansible_private_key_file": d["identity_file"],
                "connection": "ssh",
                "ansible_ssh_common_args": " ".join(self.ssh_connection_options),
            }
        except StopIteration:
            return {}
        except IOError:
            return {}

    def template_dir(self):
        return os.path.join(
            os.path.dirname(__file__),
            "cookiecutter/scenario/driver/{}".format(self.name),
        )

    def _get_instance_config(self, instance_name):
        instance_config_dict = util.safe_load_file(self._config.driver.instance_config)

        return next(
            item for item in instance_config_dict if item["instance"] == instance_name
        )

    @lru_cache()
    def sanity_checks(self):
        """Hetzner Cloud driver sanity checks."""

        log.info("Sanity checks: '{}'".format(self._name))

        try:
            import hcloud  # noqa
        except ImportError:
            msg = (
                "Missing Hetzner Cloud driver dependency. Please "
                "install the 'molecule-hetznercloud' package or "
                "refer to your INSTALL.rst driver documentation file"
            )
            sysexit_with_message(msg)

        if "HCLOUD_TOKEN" not in os.environ:
            msg = (
                "Missing Hetzner Cloud API token. Please expose "
                "the HCLOUD_TOKEN environment variable with your "
                "account API token value"
            )
            sysexit_with_message(msg)
