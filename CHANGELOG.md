# Changelog

## [v2.5.0](https://github.com/ansible-community/molecule-hetznercloud/releases/tag/v2.5.0)

While this release drops support for older versions of molecule, users may still use them. We only stopped testing the older versions of molecule in our CI.

### Features

- drop support for molecule v5 and v6 (#169)

### Bug Fixes

- ansible-core 2.19 compatibility (#180)

## [v2.4.1](https://github.com/ansible-community/molecule-hetznercloud/releases/tag/v2.4.1)

### Bug Fixes

- invalid package repository url (#165)

## [v2.4.0](https://github.com/ansible-community/molecule-hetznercloud/releases/tag/v2.4.0)

### Features

- add support for molecule 25 (#148)
- add support for python 3.13 (#155)

## [2.3.2](https://github.com/ansible-community/molecule-hetznercloud/compare/2.3.1...2.3.2) (2025-01-13)


### Bug Fixes

* relax molecule version range ([#136](https://github.com/ansible-community/molecule-hetznercloud/issues/136)) ([f0d176c](https://github.com/ansible-community/molecule-hetznercloud/commit/f0d176c19c3dce98633f6766c759643c41b7a95e)), closes [#135](https://github.com/ansible-community/molecule-hetznercloud/issues/135)

## [2.3.1](https://github.com/ansible-community/molecule-hetznercloud/compare/2.3.0...2.3.1) (2024-10-08)


### Bug Fixes

* **deps:** update dependency molecule to &gt;=5.0.0,&lt;24.10 ([#119](https://github.com/ansible-community/molecule-hetznercloud/issues/119)) ([0c8027d](https://github.com/ansible-community/molecule-hetznercloud/commit/0c8027db126bf0603bc27fb5017425855235e3a3))

## [2.3.0](https://github.com/ansible-community/molecule-hetznercloud/compare/2.2.0...2.3.0) (2024-08-19)


### Features

* require python&gt;=3.10 ([#108](https://github.com/ansible-community/molecule-hetznercloud/issues/108)) ([a623c02](https://github.com/ansible-community/molecule-hetznercloud/commit/a623c02e2ee9dbf4e0a374eec2960fad5702ad7c))


### Dependencies

* update pre-commit hook pycqa/flake8 to v7.1.0 ([e33c1af](https://github.com/ansible-community/molecule-hetznercloud/commit/e33c1af40d8a8d17f7508ffa87413c3d2ec634da))
* update pypa/gh-action-pypi-publish action to v1.9.0 ([#104](https://github.com/ansible-community/molecule-hetznercloud/issues/104)) ([bf0ca8a](https://github.com/ansible-community/molecule-hetznercloud/commit/bf0ca8a5508db0d718faff9d606c18c46365d17e))

## [2.2.0](https://github.com/ansible-community/molecule-hetznercloud/compare/2.1.1...2.2.0) (2024-06-11)


### Features

* instance `server_type` now defaults to `cx22` ([#99](https://github.com/ansible-community/molecule-hetznercloud/issues/99)) ([b1bb242](https://github.com/ansible-community/molecule-hetznercloud/commit/b1bb24242272e2d8cfd82c6efde86f90994162c0))


### Dependencies

* update dependency molecule to &gt;=5.0.0,&lt;24.7 ([#98](https://github.com/ansible-community/molecule-hetznercloud/issues/98)) ([eb56da9](https://github.com/ansible-community/molecule-hetznercloud/commit/eb56da94eb088dbd5549882c294fe0207853670f))
* update dependency pytest-cov to v5 ([#92](https://github.com/ansible-community/molecule-hetznercloud/issues/92)) ([3cde3ca](https://github.com/ansible-community/molecule-hetznercloud/commit/3cde3ca9a028ce4c1a1c8e1caaa1086f5074b328))
* update pre-commit hook asottile/pyupgrade to v3.15.1 ([#83](https://github.com/ansible-community/molecule-hetznercloud/issues/83)) ([76cd33f](https://github.com/ansible-community/molecule-hetznercloud/commit/76cd33f77867fff898aac534e062e552e5aef401))
* update pre-commit hook asottile/pyupgrade to v3.15.2 ([26bfb65](https://github.com/ansible-community/molecule-hetznercloud/commit/26bfb652fbe87177b107e00ab69c66f80e728095))
* update pre-commit hook asottile/pyupgrade to v3.16.0 ([292dda1](https://github.com/ansible-community/molecule-hetznercloud/commit/292dda12a67a08ce453d1f235085810e8f1826fe))
* update pre-commit hook pre-commit/pre-commit-hooks to v4.6.0 ([73035ce](https://github.com/ansible-community/molecule-hetznercloud/commit/73035ce0da0b474f118b4fb386b56bde1d3722af))
* update pre-commit hook psf/black-pre-commit-mirror to v24.2.0 ([#82](https://github.com/ansible-community/molecule-hetznercloud/issues/82)) ([96030aa](https://github.com/ansible-community/molecule-hetznercloud/commit/96030aa38bb0cfb4c68301cab0f50ef73cf30ac5))
* update pre-commit hook psf/black-pre-commit-mirror to v24.3.0 ([a8fce1f](https://github.com/ansible-community/molecule-hetznercloud/commit/a8fce1f11f23ad78c5c0746fe2191d91484d4e68))
* update pre-commit hook psf/black-pre-commit-mirror to v24.4.0 ([41225db](https://github.com/ansible-community/molecule-hetznercloud/commit/41225db7d216fcd9a35afa352679f05cbd6d132f))
* update pre-commit hook psf/black-pre-commit-mirror to v24.4.1 ([#95](https://github.com/ansible-community/molecule-hetznercloud/issues/95)) ([06df822](https://github.com/ansible-community/molecule-hetznercloud/commit/06df8229c11775bace06fed18657be2244a9ec65))
* update pre-commit hook psf/black-pre-commit-mirror to v24.4.2 ([e03b63e](https://github.com/ansible-community/molecule-hetznercloud/commit/e03b63e9c035636df0bca464dc124e876d460d15))
* update pypa/gh-action-pypi-publish action to v1.8.12 ([#87](https://github.com/ansible-community/molecule-hetznercloud/issues/87)) ([440c71d](https://github.com/ansible-community/molecule-hetznercloud/commit/440c71d8273b47985d0113ac26de8edf20fdab6f))
* update pypa/gh-action-pypi-publish action to v1.8.14 ([#88](https://github.com/ansible-community/molecule-hetznercloud/issues/88)) ([c1f46bb](https://github.com/ansible-community/molecule-hetznercloud/commit/c1f46bba686f7369931441b3ebe24ab9eeb6c674))

## [2.1.1](https://github.com/ansible-community/molecule-hetznercloud/compare/2.1.0...2.1.1) (2024-02-09)


### Dependencies

* update dependency molecule to v24 ([#81](https://github.com/ansible-community/molecule-hetznercloud/issues/81)) ([30516de](https://github.com/ansible-community/molecule-hetznercloud/commit/30516deaeec7643c4f6f2708c68eef3cfec55251))

## [2.1.0](https://github.com/ansible-community/molecule-hetznercloud/compare/2.0.0...2.1.0) (2024-02-02)


### Features

* change the generated ssh key type to `ed25519` ([#69](https://github.com/ansible-community/molecule-hetznercloud/issues/69)) ([2b6ab8a](https://github.com/ansible-community/molecule-hetznercloud/commit/2b6ab8a481f3f9d25172b6a564495fe7499a940c))
* enable support for python 3.12 ([#50](https://github.com/ansible-community/molecule-hetznercloud/issues/50)) ([f665af4](https://github.com/ansible-community/molecule-hetznercloud/commit/f665af4d62b0daf7ce0ae4a3b42ad8484659226d))

## [2.0.0](https://github.com/ansible-community/molecule-hetznercloud/compare/1.3.0...v2.0.0) (2023-10-09)

### ⚠ BREAKING CHANGES

- the instance volumes now require a `name`
- the molecule driver drops support for python version <3.9
- the molecule driver drops support for molecule version <5.0
- the molecule driver name was renamed from `hetznercloud` to `molecule_hetznercloud`
- rewrite hetznercloud molecule driver ([#46](https://github.com/ansible-community/molecule-hetznercloud/issues/46))

### Features

- allow user defined RESOURCE_NAMESPACE ([#54](https://github.com/ansible-community/molecule-hetznercloud/issues/54)) ([1efd919](https://github.com/ansible-community/molecule-hetznercloud/commit/1efd919552d0507a21945efcdf4799aeee821065))
- instance `server_type` now defaults to `cx11` ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- rename driver name to `molecule_hetznercloud` ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- require instance volumes name ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- require molecule &gt;=5.0,&lt;7.0 ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- require python&gt;=3.9 ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- rewrite hetznercloud molecule driver ([#46](https://github.com/ansible-community/molecule-hetznercloud/issues/46)) ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- update driver schema ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))

### Bug Fixes

- remove ansible-compat dependency ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- remove unused dependencies ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))

### Documentation

- add project history ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))
- the hetzner.hcloud collection require ansible-core&gt;=2.13 ([36a28f4](https://github.com/ansible-community/molecule-hetznercloud/commit/36a28f40da6b98eb7473739cf0edc0989f89b978))

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
