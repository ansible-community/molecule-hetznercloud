# Molecule Hetzner Cloud Plugin

[![Drone CI-CD](https://drone.autonomic.zone/api/badges/autonomic-cooperative/molecule-hetznercloud/status.svg)](https://drone.autonomic.zone/autonomic-cooperative/molecule-hetznercloud)
[![PyPI Package](https://badge.fury.io/py/molecule-hetznercloud.svg)](https://badge.fury.io/py/molecule-hetznercloud)
[![Repository License](https://img.shields.io/badge/license-LGPL-brightgreen.svg)](LICENSE)

A [Hetzner Cloud](https://www.hetzner.com/cloud) plugin for [Molecule](https://molecule.readthedocs.io/en/latest/).

This plugin allows you to do `molecule init role myrolename -d hetznercloud`
and have Molecule provision on-demand Hetzner Cloud VPSes of your choice for
your integration testing. New VPSes will be automagically created and
provisioned on each `molecule test` run, SSH keys are generated and managed
internally and all resources are cleaned up regardless of whether the role
under test succeeds or fails.

## Support

If you use this plugin in a commercial setting or you find it personally
useful, please support my maintenance work financially through my
[Liberapay](https://liberapay.com/decentral1se/) profile or through my [Github
Sponsor profile](https://github.com/sponsors/decentral1se). I do not receive
any financial support from RedHat or Hetzner Cloud for this work.

## Install

```bash
$ pip install molecule-hetznercloud
```

## Upgrade

Please see the [CHANGELOG.md](./CHANGELOG.md) for migration guides.

```bash
$ pip install --upgrade molecule-hetznercloud
```

## Usage

You need to expose a `HCLOUD_TOKEN` environment variable in your environment.

Find out more about how to get one of those [over here](https://docs.hetzner.cloud/#overview-authentication).

```bash
$ export HCLOUD_TOKEN=mycoolapitoken
```

Then create a role using the driver plugin.

```bash
$ molecule init role myrolename -d hetznercloud
```

Your `myrolename/molecule/default/molecule.yml` should then look like the following.

```yaml
---
dependency:
  name: galaxy
driver:
  name: hetznercloud
platforms:
  - name: instance
    server_type: cx11
    image: debian-10
provisioner:
  name: ansible
verifier:
  name: ansible
```

Please see [docs.hetzner.cloud](https://docs.hetzner.cloud/) for information regarding images and server types.

Then just run the role.

```bash
$ cd myrolename && molecule test
```

To ease initial debugging for getting things started, also expose the following
environment variables.

```bash
$ export MOLECULE_NO_LOG=False  # not so verbose, helpful
$ export MOLECULE_DEBUG=True  # very verbose, last ditch effort
```

## Volume Handling

It is possible to have the driver manage volumes during the test run.

You can add the following stanza to your Molecule configuration to have
Molecule create this volume for the managed VPS. This volume will be cleaned up
after use (**Please note**: there is a bug raised against clean-up right now,
see [#24](https://github.com/ansible-community/molecule-hetznercloud/issues/24)
for more).

```yaml
platforms:
  - name: instance
    server_type: cx11
    image: debian-10
    volumes:
      - name: "molecule-hetznercloud-volume-1-${INSTANCE_UUID}"
        location: /foo/bar
      - name: "molecule-hetznercloud-volume-2-${INSTANCE_UUID}"
        size: 20
```

Supported keys are:

- **name** (required): name of volume
- **size** (optional, default: `10GB`): size of volume
- **location** (optional, default: `omitted`): path for volume

## Network Creation

This Driver is able to generate networks and subnetworks during the test run.
This can be useful for cluster tests.

You can create networks with the following snippet:

```yaml
platforms:
  - name: instance1
    server_type: cx11
    image: debian-10
    networks:
      test-network:
        ip_range: 10.10.0.0/16
        subnet:
          ip: 10.10.10.1/24
          type: cloud
          network_zone: eu-central
      test-network-2:
        ip_range: 10.20.0.0/16
        subnet:
          ip: 10.20.10.1/24
  - name: instance2
    server_type: cx11
    image: debian-10
    networks:
      test-network:
        subnet:
          ip: 10.10.10.2/24
```

The networks **ip_range** is only important for creating.
If you have multiple hosts, it is okay to only define **ip_range** once.

Supported keys are:

**networks**
- **ip_range** (required): ip range of network (usually /16)

**subnet**
- **ip** (required): ip that should be assigned to host (also generates subnetwork) - prefix mandatory
- **type** (optional, default: `cloud`): type of subnetwork
- **network_zone** (optional, default: `eu-central`): network zone of subnetwork

## Only use `molecule.yml` for configuration

It is being worked on that it is possible to remove all the files except the
`molecule.yml` scenario file in your scenario directory. This is useful when
you only require this plugin to do the default behaviour each time. It is also
useful to reduce maintenance effort for migration of configurations. This
plugin currently embeds the `create.yml` and `destroy.yml` playbooks. All other
playbooks (e.g. prepare, cleanup) can be created as needed and Molecule will
pick them up and run them. Embedding the `converge.yml` awaits [this feature
request](https://github.com/ansible-community/molecule/issues/2675).

## Mirroring

Issues will be responded to on both issue trackers.

- [git.autonomic.zone](https://git.autonomic.zone/autonomic-cooperative/molecule-hetznercloud) (primary)
- [github.com](https://github.com/ansible-community/molecule-hetznercloud) (mirror)

## Change log

See [CHANGELOG.md](./CHANGELOG.md).

## Molecule Documentation

> https://molecule.readthedocs.io

## Contact

- Ping @decentral1se on the `#ansible-molecule` channel on [Freenode](https://webchat.freenode.net).

## License

The [LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.en.html) license.

## Testing

This is all done on our [drone.autonomic.zone](https://drone.autonomic.zone/autonomic-cooperative/molecule-hetznercloud) setup.

### Unit

```bash
$ pip install tox
$ tox -v
```

### Integration

Only doable by [Autonomic Cooperative](https://autonomic.zone/) members.

```bash
$ sudo apt install -y direnv
$ cp .envrc.sample .envrc
$ direnv allow
$ pip install -e . ansible
$ cd integration && molecule test
```
