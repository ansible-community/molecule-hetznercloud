import os
import shutil

import pexpect
import pkg_resources
import pytest
from molecule import logger, util

from ..conftest import change_dir_to

LOG = logger.get_logger(__name__)

IS_TRAVIS = os.getenv("TRAVIS") and os.getenv("CI")


def _env_vars_exposed(env_vars, env=os.environ):
    """Check if environment variables are exposed and populated."""
    for env_var in env_vars:
        if env_var not in os.environ:
            return False
        return os.environ[env_var] != ""


@pytest.fixture
def with_scenario(request, scenario_to_test, driver_name, scenario_name, skip_test):
    scenario_directory = os.path.join(
        os.path.dirname(util.abs_path(__file__)),
        os.path.pardir,
        "scenarios",
        scenario_to_test,
    )

    with change_dir_to(scenario_directory):
        yield
        if scenario_name:
            msg = "CLEANUP: Destroying instances for all scenario(s)"
            LOG.info(msg)
            cmd = ["molecule", "destroy", "--driver-name", driver_name, "--all"]
            pytest.helpers.run_command(cmd)


@pytest.fixture
def skip_test(request, driver_name):
    msg_tmpl = (
        "Ignoring '{}' tests for now"
        if driver_name == "delegated"
        else "Skipped '{}' not supported"
    )
    support_checks_map = {
        "hetznercloud": lambda: min_ansible("2.8") and supports_hetznercloud()
    }
    try:
        check_func = support_checks_map[driver_name]
        if not check_func():
            pytest.skip(msg_tmpl.format(driver_name))
    except KeyError:
        pass


@pytest.helpers.register
def idempotence(scenario_name):
    cmd = ["molecule", "create", "--scenario-name", scenario_name]
    pytest.helpers.run_command(cmd)

    cmd = ["molecule", "converge", "--scenario_name", scenario_name]
    pytest.helpers.run_command(cmd)

    cmd = ["molecule", "--scenario_name", scenario_name]
    pytest.helpers.run_command(cmd)


@pytest.helpers.register
def init_role(temp_dir, driver_name):
    cmd = ["molecule", "init", "role", "test-init", "--driver-name", driver_name]
    pytest.helpers.run_command(cmd)

    role_directory = os.path.join(temp_dir.strpath, "test-init")
    pytest.helpers.metadata_lint_update(role_directory)

    with change_dir_to(role_directory):
        cmd = ["molecule", "test", "--all"]
        pytest.helpers.run_command(cmd)


@pytest.helpers.register
def init_scenario(temp_dir, driver_name):
    cmd = ["molecule", "init", "role", "test-init", "--driver-name", driver_name]
    pytest.helpers.run_command(cmd)

    role_directory = os.path.join(temp_dir.strpath, "test-init")
    pytest.helpers.metadata_lint_update(role_directory)

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, "test-scenario")

        cmd = [
            "molecule",
            "init",
            "scenario",
            "test-scenario",
            "--role-name",
            "test-init",
            "--driver-name",
            driver_name,
        ]
        pytest.helpers.run_command(cmd)

        assert os.path.isdir(scenario_directory)

        cmd = ["molecule", "test", "--scenario-name", "test-scenario", "--all"]
        pytest.helpers.run_command(cmd)


@pytest.helpers.register
def metadata_lint_update(role_directory):
    ansible_lint_src = os.path.join(
        os.path.dirname(util.abs_path(__file__)), ".ansible-lint"
    )

    shutil.copy(ansible_lint_src, role_directory)

    with change_dir_to(role_directory):
        cmd = ["ansible-lint", "."]
    pytest.helpers.run_command(cmd)


@pytest.helpers.register
def list(x):
    cmd = ["molecule", "list"]
    out = pytest.helpers.run_command(cmd, log=False)
    out = out.stdout.decode("utf-8")
    out = util.strip_ansi_color(out)

    for l in x.splitlines():
        assert l in out


@pytest.helpers.register
def list_with_format_plain(x):
    cmd = ["molecule", "list", "--format", "plain"]
    result = util.run_command(cmd)
    out = util.strip_ansi_color(result.stdout)

    for l in x.splitlines():
        assert l in out


@pytest.helpers.register
def login(login_args, scenario_name="default"):
    cmd = ["molecule", "destroy", "--scenario-name", scenario_name]
    pytest.helpers.run_command(cmd)

    cmd = ["molecule", "create", "--scenario-name", scenario_name]
    pytest.helpers.run_command(cmd)

    for instance, regexp in login_args:
        if len(login_args) > 1:
            child_cmd = "molecule login --host {} --scenario-name {}".format(
                instance, scenario_name
            )
        else:
            child_cmd = "molecule login --scenario-name {}".format(scenario_name)
        child = pexpect.spawn(child_cmd)
        child.expect(regexp)
        child.sendline("exit")


@pytest.helpers.register
def test(driver_name, scenario_name="default", parallel=False):
    cmd = ["molecule", "test", "--scenario-name", scenario_name]

    if driver_name != "delegated":
        if scenario_name is None:
            cmd.append("--all")
        if parallel:
            cmd.append("--parallel")

    pytest.helpers.run_command(cmd)


@pytest.helpers.register
def verify(scenario_name="default"):
    cmd = ["molecule", "create", "--scenario-name", scenario_name]
    pytest.helpers.run_command(cmd)

    cmd = ["molecule", "converge", "--scenario-name", scenario_name]
    pytest.helpers.run_command(cmd)

    cmd = ["molecule", "verify", "--scenario-name", scenario_name]
    pytest.helpers.run_command(cmd)


def min_ansible(version):
    """Ensure current Ansible is newer than a given a minimal one."""
    try:
        from ansible.release import __version__

        return pkg_resources.parse_version(__version__) >= pkg_resources.parse_version(
            version
        )
    except ImportError as exception:
        LOG.error("Unable to parse Ansible version", exc_info=exception)
        return False


@pytest.helpers.register
def supports_hetznercloud():
    pytest.importorskip("hcloud")

    env_vars = ("HCLOUD_TOKEN",)

    return _env_vars_exposed(env_vars)
