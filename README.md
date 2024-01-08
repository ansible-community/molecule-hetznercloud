# Molecule Hetzner Cloud Driver

[![PyPI Package](https://img.shields.io/pypi/v/molecule-hetznercloud)](https://pypi.org/project/molecule-hetznercloud/)
[![Codecov](https://img.shields.io/codecov/c/github/ansible-community/molecule-hetznercloud/main)](https://app.codecov.io/gh/ansible-community/molecule-hetznercloud/tree/main)
[![License](https://img.shields.io/badge/license-LGPL-brightgreen.svg)](LICENSE)

A [Hetzner Cloud](https://www.hetzner.com/cloud) driver for [Molecule](https://ansible.readthedocs.io/projects/molecule/).

This plugin allows you to use on-demand Hetzner Cloud servers for your molecule integration tests.

## Install

```bash
$ pip install molecule-hetznercloud
```

## Upgrade

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

```bash
$ pip install --upgrade molecule-hetznercloud
```

### Upgrading to v2

- In your `molecule.yml` files, rename the molecule driver name (`driver.name`) to `molecule_hetznercloud`:

```patch
 driver:
-  name: hetznercloud
+  name: molecule_hetznercloud
```

- In your `molecule.yml` files, the volumes name (`platforms[].volumes[].name`) field is now required. If the field is missing, you MUST add it:

```patch
 platforms:
   - name: instance-1
     image: debian-12
     volumes:
-     - size: 20
+     - name: volume-1
+       size: 20
```

- Each resource (servers, volumes, networks) name are prefixed with a hash (32 chars) based on the role and scenario path. This means you MAY reuse the same names (e.g. `instance-1`) across your scenarios. Resource names MUST not exceed their max length, for example the server name max length is 63 chars, with the prefix you only have 31 chars left for your name.

- In your `molecule.yml` files, the platforms server type (`platforms[].server_type`) field now defaults to `cx11`. If you already use the default, you MAY remove the field:

```patch
 platforms:
   - name: instance-1
     image: debian-12
-    server_type: cx11
```

## Usage

To communicate with the Hetzner Cloud API, you need to expose a `HCLOUD_TOKEN` environment variable. Find out more about how to get a Hetzner Cloud API token in the [authentication documentation](https://docs.hetzner.cloud/#authentication).

```bash
$ export HCLOUD_TOKEN="set_the_hcloud_token_here"
```

Then setup a new molecule scenario using the driver plugin.

```bash
$ molecule init scenario --driver-name molecule_hetznercloud
```

> [!WARNING]
> With molecule 6, the `molecule init scenario` command dropped support for driver provided configuration. If you are using molecule >=6, please copy the example below and paste it in your scenario `molecule.yml` file.
> See [this commit](https://github.com/ansible/molecule/commit/21dcd2bb7e8e9002be8bbc19de3e66ec3ce586f1) for details.

Your `molecule/default/molecule.yml` should then look like the following.

```yaml
---
driver:
  name: molecule_hetznercloud
platforms:
  - # Name of the Server to create (must be unique per Project and a valid hostname as per RFC 1123).
    # required
    name: instance-1
    # Name of the Image the Server is created from.
    # required
    image: debian-12
    # Name of the Server type this Server should be created with.
    # default: cx11
    server_type: cx11
    # Name of Location to create Server in (must not be used together with datacenter).
    # default: omit
    location: hel1
    # Name of Datacenter to create Server in (must not be used together with location).
    # default: omit
    datacenter: null
    # Cloud-Init user data to use during Server creation. This field is limited to 32KiB.
    # default: omit
    user_data: null

    # List of volumes to attach to the server.
    volumes:
      - # Name of the volume.
        # required
        name: volume-1
        # Size of the Volume in GB.
        # default: 10
        size: 10

    # Dictionary of private networks the server should be attached to.
    networks:
      # Name of the network
      network-1:
        # IP range of the whole network which must span all included subnets. Must be one of the private IPv4 ranges of RFC1918.
        # If multiple hosts using the same network, you may only define it once.
        # required
        ip_range: 10.0.0.0/16
        subnet:
          # IP to assign to the server.
          # required
          ip: 10.0.0.1/24
          # Type of subnetwork.
          # default: cloud
          type: cloud
          # Name of network zone.
          # default: eu-central
          network_zone: eu-central
      network-2:
        ip_range: 10.1.0.0/16
        subnet:
          ip: 10.1.0.1/24
```

> [!NOTE]
> The `networks.ip_range` is important for creating. If you have multiple
> hosts, you may only define it once.

> [!NOTE]
> You may list the server types and available images using the `hcloud` command line tool:
>
> ```bash
> # List server types
> $ hcloud server-type list --sort name
> # List images for the x86 architecture
> $ hcloud image list --type system --architecture x86 --sort name
> ```

Then test your role.

```bash
$ molecule test
```

To ease initial debugging for getting things started, also expose the following
environment variables.

```bash
$ export MOLECULE_NO_LOG=False  # not so verbose, helpful
$ export MOLECULE_DEBUG=True  # very verbose, last ditch effort
```

You may also define a custom resource namespace by exposing the following
environment variables, for example in CI workflows:

```bash
$ export RESOURCE_NAMESPACE=e121dc64ff615ccdfac71bb5c00296b9 # Ensure the value length is <= 32
```

## Development

### Testing

Run unit tests:

```bash
make test
```

Run integration tests

```bash
export HCLOUD_TOKEN="set_the_hcloud_token_here"
make integration
```

## History

The project was initially maintained by [@decentral1se](https://github.com/decentral1se). After a long period [looking for new maintainers](https://github.com/ansible-community/molecule-hetznercloud/issues/43), the project was archived in early 2023.

In September 2023, the code has been rewritten by [@jooola](https://github.com/jooola) and the project was reactivated to continue development.

## License

The [LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.en.html) license.
