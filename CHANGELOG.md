# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.1] - 2021-06-02

- Remove async task handling for network deletion ([#30](https://github.com/ansible-community/molecule-hetznercloud/pull/30), credit @ggggut)

## [1.2.0] - 2021-06-02

- Allow to create networks during test runs ([#29](https://github.com/ansible-community/molecule-hetznercloud/pull/29), thanks @ggggut!)

## [1.1.0] - 2021-03-30

## Changed

- Relaxed bounds on Molecule to allow all versions < v4 ([#27](https://github.com/ansible-community/molecule-hetznercloud/pull/27))

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

## Fixed

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
