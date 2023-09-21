import os

from pytest_ansible.molecule import MoleculeScenario


def test_integration(molecule_scenario: MoleculeScenario) -> None:
    """
    Run molecule for each scenario.
    """
    assert "HCLOUD_TOKEN" in os.environ

    proc = molecule_scenario.test()
    assert proc.returncode == 0
