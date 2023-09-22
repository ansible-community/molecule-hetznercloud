from __future__ import annotations

from shutil import copytree

from molecule.util import run_command

from ..conftest import change_dir
from .fixtures import here as fixtures_path


def test_command_init_scenario(tmp_path):
    role_name = "test_init_scenario"
    scenario_name = "test_scenario"

    role_path = tmp_path / role_name
    copytree(fixtures_path / role_name, role_path)

    with change_dir(role_path):
        cmd = [
            "molecule",
            "init",
            "scenario",
            scenario_name,
            "--driver-name",
            "molecule_hetznercloud",
        ]
        result = run_command(cmd)
        assert result.returncode == 0

    scenario_path = role_path / "molecule" / scenario_name
    assert scenario_path.is_dir()
    assert (scenario_path / "molecule.yml").is_file()
    assert (scenario_path / "destroy.yml").is_file()
    assert (scenario_path / "converge.yml").is_file()
    assert (scenario_path / "create.yml").is_file()
