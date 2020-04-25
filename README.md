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

## Usage

You need to expose a `HCLOUD_TOKEN` environment variable in your environment.
Find out more about how to get one of those [over here](https://docs.hetzner.cloud/#overview-authentication).

```bash
$ export HCLOUD_TOKEN=mycoolapitoken
```

Then install the required Python package.

```bash
$ pip install molecule-hetznercloud
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
  - name: my-instance-name
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

To ease initial debugging for getting thing started, also expose the following
environment variables.

```bash
$ export MOLECULE_NO_LOG=False  # not so verbose, helpful
$ export MOLECULE_DEBUG=True  # very verbose, last ditch effort
```

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

Unit tests and such.

```bash
$ pip install tox
$ tox -v
```

Integration tests.

(Only doable by [Autonomic Cooperative](https://autonomic.zone/) members.)

```bash
$ sudo apt install -y direnv
$ cp .envrc.sample .envrc
$ direnv allow
$ pip install -e .
$ cd integration-test-role && molecule test
```
