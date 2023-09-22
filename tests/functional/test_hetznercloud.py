from __future__ import annotations

from pathlib import Path
from shutil import copytree

import pytest
from molecule._version import version_tuple as molecule_version_tuple
from molecule.util import run_command

import molecule_hetznercloud

from ..conftest import change_dir
from .fixtures import here as fixtures_path

here = Path(__file__).parent

package_path = Path(molecule_hetznercloud.__file__).parent
templates_path = (
    package_path
    / "cookiecutter/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}"
)


@pytest.mark.skipif(
    molecule_version_tuple >= (6, 0),
    reason="molecule 6 removed support for custom templates from drivers ",
)
def test_command_init_scenario(tmp_path):
    role_name = "test_init_scenario"
    scenario_name = "default"

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
    molecule_path = scenario_path / "molecule.yml"
    converge_path = scenario_path / "converge.yml"

    assert scenario_path.is_dir()
    assert molecule_path.is_file()
    assert converge_path.is_file()

    assert molecule_path.read_text() == (templates_path / "molecule.yml").read_text()
