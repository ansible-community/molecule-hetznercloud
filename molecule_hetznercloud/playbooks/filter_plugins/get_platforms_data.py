#!/usr/bin/env python


from __future__ import annotations


def merge_two_dicts(x: dict, y: dict) -> dict:
    z = x.copy()
    z.update(y)
    return z


def get_hetznercloud_networks(platforms: list[dict]) -> list:
    all_networks = {}
    for platform in platforms:
        if "networks" not in platform:
            continue

        for network_name, network in platform["networks"].items():
            if network is None:
                continue
            network["name"] = network_name

            del network["subnet"]

            existing_network = all_networks.get(network_name, {})
            all_networks[network_name] = merge_two_dicts(existing_network, network)

    return list(all_networks.values())


def get_hetznercloud_subnetworks(platforms: list[dict]) -> list[dict]:
    all_subnetworks = []
    for platform in platforms:
        if "networks" not in platform:
            continue

        for network_name, network in platform["networks"].items():
            network["name"] = network_name
            if "subnet" in network:
                network["subnet"]["server_name"] = platform["name"]
                network["subnet"]["network_name"] = network_name
                all_subnetworks.append(network["subnet"])

    return all_subnetworks


def get_hetznercloud_volumes(platforms: list[dict]) -> list[dict]:
    all_volumes = []
    for platform in platforms:
        if "volumes" not in platform:
            continue

        for volume in platform["volumes"]:
            volume["server_name"] = platform["name"]
            all_volumes.append(volume)

    return all_volumes


class FilterModule:
    """Core Molecule filter plugins."""

    def filters(self):
        return {
            "molecule_get_hetznercloud_networks": get_hetznercloud_networks,
            "molecule_get_hetznercloud_subnetworks": get_hetznercloud_subnetworks,
            "molecule_get_hetznercloud_volumes": get_hetznercloud_volumes,
        }
