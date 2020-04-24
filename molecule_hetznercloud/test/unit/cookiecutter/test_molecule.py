import os

import pytest
import sh

from molecule import util
from molecule.command.init import base
from molecule.model import schema_v3


class CommandBase(base.Base):
    pass


@pytest.fixture
def _base_class():
    return CommandBase


@pytest.fixture
def _instance(_base_class):
    return _base_class()


@pytest.fixture
def _command_args():
    return {
        "dependency_name": "galaxy",
        "driver_name": "hetznercloud",
        "provisioner_name": "ansible",
        "scenario_name": "default",
        "role_name": "test-role",
        "verifier_name": "testinfra",
    }


@pytest.fixture
def _role_directory():
    return "."


@pytest.fixture
def _molecule_file(_role_directory):
    return os.path.join(
        _role_directory, "test-role", "molecule", "default", "molecule.yml"
    )


@pytest.mark.parametrize("driver", [("hetznercloud")])
def test_drivers(
    driver, temp_dir, _molecule_file, _role_directory, _command_args, _instance
):
    _command_args["driver_name"] = driver
    _instance._process_templates("molecule", _command_args, _role_directory)

    data = util.safe_load_file(_molecule_file)

    assert {} == schema_v3.validate(data)

    cmd = sh.yamllint.bake("-s", _molecule_file)
    pytest.helpers.run_command(cmd)
