SHELL := bash

venv:
	python3 -m venv venv
	venv/bin/pip install -e .[test]

export ANSIBLE_COLLECTIONS_PATH = $(shell pwd)/ansible_collections

ansible_collections: venv
	venv/bin/ansible-galaxy collection install -r requirements.yml

.PHONY: test
test: venv
	venv/bin/tox -- tests/functional tests/unit

.PHONY: integration
integration: venv ansible_collections
	venv/bin/tox -- tests/integration

.PHONY: clean
clean:
	git clean -xdf
