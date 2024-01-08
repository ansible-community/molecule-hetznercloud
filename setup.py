from __future__ import annotations

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()


version_vars = {}
with open("molecule_hetznercloud/_version.py", encoding="utf-8") as fp:
    exec(fp.read(), version_vars)


setup(
    name="molecule-hetznercloud",
    version=version_vars["__version__"],
    keywords="ansible molecule driver hcloud hetzner cloud testing",
    description="Molecule driver for Hetzner Cloud",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Hetzner Cloud GmbH",
    author_email="support-cloud@hetzner.com",
    url="https://github.com/hetznercloud/hcloud-python",
    project_urls={
        "Bug Tracker": "https://github.com/ansible-community/molecule-hetznercloud/issues",
        "Documentation": "https://github.com/ansible-community/molecule-hetznercloud#readme",
        "Changelog": "https://github.com/ansible-community/molecule-hetznercloud/blob/main/CHANGELOG.md",
        "Source Code": "https://github.com/ansible-community/molecule-hetznercloud",
    },
    license="LGPL",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
    install_requires=[
        "molecule>=5.0.0,<7.0",
        # Dependencies for the hetzner.hcloud collection
        "python-dateutil>=2.7.5",
        "requests>=2.20",
        # Dependencies for the ansible.utils collection (ansible.utils.ipaddr)
        "netaddr",
    ],
    extras_require={
        "test": [
            "tox>=4.11.3,<5.0",
            "pytest-xdist>=3.3.1,<4.0",
            "pytest>=7.4.0,<8.0",
            "pytest-ansible>=4.1.0,<5.0",
            "pytest-cov>=4.1.0 ,<5.0",
        ],
    },
    packages=find_packages(exclude=["tests*"]),
    package_data={
        "": [
            "**/*.json",
            "**/*.py",
            "**/*.rst",
            "**/*.yml",
        ]
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "molecule.driver": [
            "molecule_hetznercloud=molecule_hetznercloud.driver:HetznerCloud",
        ]
    },
)
