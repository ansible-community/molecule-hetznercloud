# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Decolonise Git praxis and use the main branch as default.

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
