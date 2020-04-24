import os

import pytest

import sh
from molecule.scenario import ephemeral_directory


@pytest.fixture
def scenario_to_test(request):
    return request.param


@pytest.fixture
def scenario_name(request):
    try:
        return request.param
    except AttributeError:
        return None


@pytest.fixture
def driver_name(request):
    return request.param


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_check(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("check", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_cleanup(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("cleanup", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_converge(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("converge", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_create(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("create", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.skip(
    reason="Disabled due to https://github.com/ansible/galaxy/issues/2030"
)
@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("dependency", "hetznercloud", "ansible-galaxy")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_dependency_ansible_galaxy(
    request, scenario_to_test, with_scenario, scenario_name
):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("dependency", **options)
    pytest.helpers.run_command(cmd)

    dependency_role = os.path.join(
        ephemeral_directory("molecule"),
        "dependency",
        "ansible-galaxy",
        "roles",
        "timezone",
    )
    assert os.path.isdir(dependency_role)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("dependency", "hetznercloud", "gilt")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_dependency_gilt(
    request, scenario_to_test, with_scenario, scenario_name
):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("dependency", **options)
    pytest.helpers.run_command(cmd)

    dependency_role = os.path.join(
        ephemeral_directory("molecule"), "dependency", "gilt", "roles", "timezone"
    )
    assert os.path.isdir(dependency_role)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("dependency", "hetznercloud", "shell")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_dependency_shell(
    request, scenario_to_test, with_scenario, scenario_name
):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("dependency", **options)
    pytest.helpers.run_command(cmd)

    dependency_role = os.path.join(
        ephemeral_directory("molecule"), "dependency", "shell", "roles", "timezone"
    )
    assert os.path.isdir(dependency_role)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_destroy(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("destroy", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_idempotence(scenario_to_test, with_scenario, scenario_name):
    pytest.helpers.idempotence(scenario_name)


@pytest.mark.parametrize("driver_name", [("hetznercloud")], indirect=["driver_name"])
def test_command_init_role(temp_dir, driver_name, skip_test):
    pytest.helpers.init_role(temp_dir, driver_name)


@pytest.mark.parametrize("driver_name", [("hetznercloud")], indirect=["driver_name"])
def test_command_init_scenario(temp_dir, driver_name, skip_test):
    pytest.helpers.init_scenario(temp_dir, driver_name)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_lint(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("lint", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, expected",
    [
        (
            "driver/hetznercloud",
            "hetznercloud",
            """
Instance Name    Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------  -------------  ------------------  ---------------  ---------  -----------
instance         hetznercloud   ansible             default          false      false
instance-1       hetznercloud   ansible             multi-node       false      false
instance-2       hetznercloud   ansible             multi-node       false      false
""".strip(),  # noqa
        )
    ],
    indirect=["scenario_to_test", "driver_name"],
)
def test_command_list(scenario_to_test, with_scenario, expected):
    pytest.helpers.list(expected)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, expected",
    [
        (
            "driver/hetznercloud",
            "hetznercloud",
            """
instance    hetznercloud  ansible  default     false  false
instance-1  hetznercloud  ansible  multi-node  false  false
instance-2  hetznercloud  ansible  multi-node  false  false
""".strip(),
        )  # noqa
    ],
    indirect=["scenario_to_test", "driver_name"],
)
def test_command_list_with_format_plain(scenario_to_test, with_scenario, expected):
    pytest.helpers.list_with_format_plain(expected)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, login_args, scenario_name",
    [
        (
            "driver/hetznercloud",
            "hetznercloud",
            [["instance-1", ".*instance-1.*"], ["instance-2", ".*instance-2.*"]],
            "multi-node",
        )
    ],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_login(scenario_to_test, with_scenario, login_args, scenario_name):
    pytest.helpers.login(login_args, scenario_name)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_prepare(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}

    cmd = sh.molecule.bake("create", **options)
    pytest.helpers.run_command(cmd)

    cmd = sh.molecule.bake("prepare", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_side_effect(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("side-effect", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_syntax(scenario_to_test, with_scenario, scenario_name):
    options = {"scenario_name": scenario_name}
    cmd = sh.molecule.bake("syntax", **options)
    pytest.helpers.run_command(cmd)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", None)],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_test(scenario_to_test, with_scenario, scenario_name, driver_name):
    pytest.helpers.test(driver_name, scenario_name)


@pytest.mark.parametrize(
    "scenario_to_test, driver_name, scenario_name",
    [("driver/hetznercloud", "hetznercloud", "default")],
    indirect=["scenario_to_test", "driver_name", "scenario_name"],
)
def test_command_verify(scenario_to_test, with_scenario, scenario_name):
    pytest.helpers.verify(scenario_name)
