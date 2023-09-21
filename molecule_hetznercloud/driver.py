import os

from molecule import logger, util
from molecule.api import Driver

log = logger.get_logger(__name__)


class HetznerCloud(Driver):
    def __init__(self, config=None):
        super().__init__(config)
        self._name = "molecule_hetznercloud"

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
            "ssh {address} "
            "-l {user} "
            "-p {port} "
            "-i {identity_file} "
            f"{connection_options}"
        )

    @property
    def default_safe_files(self):
        return [self.instance_config, "ssh_key"]

    @property
    def default_ssh_connection_options(self):
        return self._get_ssh_connection_options()

    def login_options(self, instance_name):
        config = {"instance": instance_name}

        return util.merge_dicts(config, self._get_instance_config(instance_name))

    def ansible_connection_options(self, instance_name):
        try:
            config = self._get_instance_config(instance_name)

            return {
                "ansible_user": config["user"],
                "ansible_host": config["address"],
                "ansible_port": config["port"],
                "ansible_private_key_file": config["identity_file"],
                "connection": "ssh",
                "ansible_ssh_common_args": " ".join(self.ssh_connection_options),
            }
        except StopIteration:
            return {}
        except OSError:
            return {}

    def template_dir(self):
        return os.path.join(
            os.path.dirname(__file__),
            f"cookiecutter/scenario/driver/{self.name}",
        )

    def _get_instance_config(self, instance_name):
        instance_config_dict = util.safe_load_file(self._config.driver.instance_config)

        return next(
            item for item in instance_config_dict if item["instance"] == instance_name
        )

    def sanity_checks(self) -> None:
        """Confirm that driver is usable.

        Sanity checks to ensure the driver can do work successfully. For
        example, when using the Docker driver, we want to know that the Docker
        daemon is running and we have the correct Docker Python dependency.
        Each driver implementation can decide what is the most stable sanity
        check for itself.

        :returns: None
        """

    def reset(self):
        """Release all resources owned by molecule.

        This is a destructive operation that would affect all resources managed
        by molecule, regardless the scenario name.  Molecule will use metadata
        like labels or tags to annotate resources allocated by it.
        """

    def schema_file(self):
        return os.path.join(os.path.dirname(__file__), "driver.json")
