import os

import pytest

from molecule import config
from molecule_hetznercloud import driver


@pytest.fixture
def hetznercloud_instance(patched_config_validate, config_instance):
    return driver.HetznerCloud(config_instance)


def test_hetznercloud_config_gives_config_object(hetznercloud_instance):
    assert isinstance(hetznercloud_instance._config, config.Config)


def test_hetznercloud_testinfra_options_property(hetznercloud_instance):
    assert {
        "connection": "ansible",
        "ansible-inventory": hetznercloud_instance._config.provisioner.inventory_file,
    } == hetznercloud_instance.testinfra_options


def test_hetznercloud_name_property(hetznercloud_instance):
    assert "hetznercloud" == hetznercloud_instance.name


def test_hetznercloud_options_property(hetznercloud_instance):
    assert {"managed": True} == hetznercloud_instance.options


def test_hetznercloud_login_cmd_template_property(hetznercloud_instance):
    template = "ssh {address} -l {user} -p {port}"
    assert template in hetznercloud_instance.login_cmd_template


def test_hetznercloud_safe_files_property(hetznercloud_instance):
    expected_safe_files = [
        os.path.join(
            hetznercloud_instance._config.scenario.ephemeral_directory,
            "instance_config.yml",
        )
    ]

    assert expected_safe_files == hetznercloud_instance.safe_files


def test_hetznercloud_default_safe_files_property(hetznercloud_instance):
    expected_default_safe_files = [
        os.path.join(
            hetznercloud_instance._config.scenario.ephemeral_directory,
            "instance_config.yml",
        )
    ]
    assert expected_default_safe_files == hetznercloud_instance.default_safe_files


def test_hetznercloud_delegated_property(hetznercloud_instance):
    assert not hetznercloud_instance.delegated


def test_hetznercloud_managed_property(hetznercloud_instance):
    assert hetznercloud_instance.managed


@pytest.mark.xfail(reason="Broken on molecule v3")
def test_hetznercloud_default_ssh_connection_options_property(hetznercloud_instance):
    expected_options = [
        "-o UserKnownHostsFile=/dev/null",
        "-o ControlMaster=auto",
        "-o ControlPersist=60s",
        "-o ForwardX11=no",
        "-o LogLevel=ERROR",
        "-o IdentitiesOnly=yes",
        "-o StrictHostKeyChecking=no",
    ]

    assert expected_options == (hetznercloud_instance.default_ssh_connection_options)


@pytest.mark.xfail(reason="Broken on molecule v3")
def test_hetznercloud_login_options(hetznercloud_instance, mocker):
    target = "molecule_hetznercloud.hetznercloud.HetznerCloud._get_instance_config"
    get_instance_config_patch = mocker.patch(target)

    get_instance_config_patch.return_value = {
        "instance": "hetznercloud",
        "address": "172.16.0.2",
        "user": "hetzner-admin",
        "port": 22,
    }

    get_instance_config_patch = {
        "instance": "hetznercloud",
        "address": "172.16.0.2",
        "user": "hetzner-admin",
        "port": 22,
    }

    assert get_instance_config_patch == hetznercloud_instance.login_options(
        "hetznercloud"
    )


@pytest.mark.xfail(reason="Broken on molecule v3")
def test_hetznercloud_ansible_connection_opts(hetznercloud_instance, mocker):
    target = "molecule_hetznercloud.hetznercloud.HetznerCloud._get_instance_config"
    get_instance_config_patch = mocker.patch(target)

    get_instance_config_patch.return_value = {
        "instance": "hetznercloud",
        "address": "172.16.0.2",
        "user": "hetzner-admin",
        "port": 22,
        "identity_file": "/foo/bar",
    }

    get_instance_config_patch = {
        "ansible_host": "172.16.0.2",
        "ansible_port": 22,
        "ansible_user": "hetzner-admin",
        "ansible_private_key_file": "/foo/bar",
        "connection": "ssh",
        "ansible_ssh_common_args": (
            "-o UserKnownHostsFile=/dev/null "
            "-o ControlMaster=auto "
            "-o ControlPersist=60s "
            "-o IdentitiesOnly=yes "
            "-o StrictHostKeyChecking=no"
        ),
    }

    connection_options = hetznercloud_instance.ansible_connection_options(
        "hetznercloud"
    )
    assert get_instance_config_patch == connection_options


def test_hetznercloud_instance_config_property(hetznercloud_instance):
    instance_config_path = os.path.join(
        hetznercloud_instance._config.scenario.ephemeral_directory,
        "instance_config.yml",
    )

    assert instance_config_path == hetznercloud_instance.instance_config


@pytest.mark.xfail(reason="Needs rewrite as it assumes to strict check")
def test_hetznercloud_ssh_connection_options_property(hetznercloud_instance):
    expected_options = [
        "-o UserKnownHostsFile=/dev/null",
        "-o ControlMaster=auto",
        "-o ControlPersist=60s",
        "-o IdentitiesOnly=yes",
        "-o StrictHostKeyChecking=no",
    ]

    assert expected_options == hetznercloud_instance.ssh_connection_options


def test_hetznercloud_status(mocker, hetznercloud_instance):
    hetzner_status = hetznercloud_instance.status()

    assert 2 == len(hetzner_status)

    assert hetzner_status[0].instance_name == "instance-1"
    assert hetzner_status[0].driver_name == "hetznercloud"
    assert hetzner_status[0].provisioner_name == "ansible"
    assert hetzner_status[0].scenario_name == "default"
    assert hetzner_status[0].created == "false"
    assert hetzner_status[0].converged == "false"

    assert hetzner_status[1].instance_name == "instance-2"
    assert hetzner_status[1].driver_name == "hetznercloud"
    assert hetzner_status[1].provisioner_name == "ansible"
    assert hetzner_status[1].scenario_name == "default"
    assert hetzner_status[1].created == "false"
    assert hetzner_status[1].converged == "false"


def test_created(hetznercloud_instance):
    assert "false" == hetznercloud_instance._created()


def test_converged(hetznercloud_instance):
    assert "false" == hetznercloud_instance._converged()
