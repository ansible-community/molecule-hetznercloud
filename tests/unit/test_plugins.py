from __future__ import annotations

from copy import deepcopy

import pytest

from molecule_hetznercloud.playbooks.filter_plugins.get_platforms_data import (
    get_hetznercloud_networks,
    get_hetznercloud_subnetworks,
    get_hetznercloud_volumes,
)


@pytest.mark.parametrize(
    ("data", "networks", "subnetworks", "volumes"),
    [
        (
            # Data
            [
                dict(
                    name="instance-1",
                    image="debian-12",
                    networks={
                        "network-1": dict(
                            ip_range="10.10.0.0/16",
                            subnet=dict(ip="10.10.10.1/24"),
                        )
                    },
                    volumes=[dict(name="volume-1"), dict(size=20)],
                )
            ],
            # Networks
            [{"name": "network-1", "ip_range": "10.10.0.0/16"}],
            # Subnetworks
            [
                {
                    "ip": "10.10.10.1/24",
                    "server_name": "instance-1",
                    "network_name": "network-1",
                }
            ],
            # Volumes
            [
                {"name": "volume-1", "server_name": "instance-1"},
                {"size": 20, "server_name": "instance-1"},
            ],
        ),
        (
            # Data
            [
                dict(
                    name="instance-1",
                    image="debian-12",
                    networks={
                        "network-1": dict(
                            ip_range="10.10.0.0/16",
                            subnet=dict(ip="10.10.10.1/24"),
                        )
                    },
                    volumes=[dict(name="volume-1")],
                ),
                dict(
                    name="instance-2",
                    image="debian-12",
                    networks={
                        "network-1": dict(
                            subnet=dict(ip="10.10.10.2/24"),
                        )
                    },
                    volumes=[dict(size=20)],
                ),
            ],
            # Networks
            [{"name": "network-1", "ip_range": "10.10.0.0/16"}],
            # Subnetworks
            [
                {
                    "ip": "10.10.10.1/24",
                    "server_name": "instance-1",
                    "network_name": "network-1",
                },
                {
                    "ip": "10.10.10.2/24",
                    "network_name": "network-1",
                    "server_name": "instance-2",
                },
            ],
            # Volumes
            [
                {"name": "volume-1", "server_name": "instance-1"},
                {"size": 20, "server_name": "instance-2"},
            ],
        ),
    ],
)
def test_get_platform_data(data, networks, subnetworks, volumes):
    found = get_hetznercloud_networks(deepcopy(data))
    assert found == networks
    found = get_hetznercloud_subnetworks(deepcopy(data))
    assert found == subnetworks
    found = get_hetznercloud_volumes(deepcopy(data))
    assert found == volumes
