# Changelog

## [1.3.0] - 2021-09-02

Changes:

- Remove deprecated molecule cache ([#35](https://github.com/ansible-community/molecule-hetznercloud/pull/35)) @ssbarnea
- Remove duplicated playbook code ([#33](https://github.com/ansible-community/molecule-hetznercloud/pull/33)) @ekeih
- Remove async for network deletion ([#30](https://github.com/ansible-community/molecule-hetznercloud/pull/30)) @ggggut
- Typo fix ([#28](https://github.com/ansible-community/molecule-hetznercloud/pull/28)) @aminvakil

Bugfixes:

- Remove deprecated molecule cache ([#35](https://github.com/ansible-community/molecule-hetznercloud/pull/35)) @ssbarnea
- Testing configuration cleanup ([#11](https://github.com/ansible-community/molecule-hetznercloud/pull/11)) @ssbarnea
- Match API expectations ([#8](https://github.com/ansible-community/molecule-hetznercloud/pull/8)) @decentral1se
- Allow Molecule to load the cookiecutter correctly ([#7](https://github.com/ansible-community/molecule-hetznercloud/pull/7)) @decentral1se
- Fix CI ([#6](https://github.com/ansible-community/molecule-hetznercloud/pull/6)) @decentral1se
- Add a missing entry point option to setup.cfg ([#5](https://github.com/ansible-community/molecule-hetznercloud/pull/5)) @tadeboro
- Enabling Travis testing ([#1](https://github.com/ansible-community/molecule-hetznercloud/pull/1)) @decentral1se

## [1.2.1] - 2021-06-02

### Fixed

- Remove async task handling for network deletion ([#30](https://github.com/ansible-community/molecule-hetznercloud/pull/30), credit @ggggut)

## [1.2.0] - 2021-06-02

### Added

- Allow to create networks during test runs ([#29](https://github.com/ansible-community/molecule-hetznercloud/pull/29), thanks @ggggut!)

## [1.1.0] - 2021-03-30

## Changed

- Relaxed bounds on Molecule to allow all versions less than `v4` ([#27](https://github.com/ansible-community/molecule-hetznercloud/pull/27))

## [1.0.0] - 2021-01-06

This is a major release with breaking changes for your schema and support for a
new major version of Molecule. If you use the `volumes:` key in your
`molecule.yml` then this change will break your configuration. Please see the
section on "Volume Handling" in the README.md on how to upgrade successfully.
You will now need to install Ansible yourself as Molecule does not do it for
you. If there are any other breaking changes, please report them on the issue
tracker so that we can mention them here.

- Support Python 3.9.
- Support Molecule 3.2.1
- Add volume creation and clean up handling

## [0.2.2] - 2020-06-15

### Fixed

- Point to an open issue tracker

## [0.2.1] - 2020-04-29

### Fixed

- Pinned Molecule to avoid issues with `sh` dependency.

## [0.2.0] - 2020-04-27

### Added

- Add bundled playbooks so as to reduce required configuration on end-user side
- Added an internal `molecule.yml` so that `molecule init role` can get good defaults (will work with Molecule >= 3.0.4)

## [0.1.0] - 2020-04-27

### Added

- py36,37,38 are now supported

## [0.0.1] - 2020-04-25

### Added

- Molecule 3.x support
- Usage documentation in the README.md
- Drone CI/CD integration testing

### Changed

- Migrate to git.autonomic.zone for maintenance
- Mirroring of Github repository and discussion with Molecule team
