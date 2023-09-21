SHELL := bash
.PHONY: integration clean

venv:
	python3 -m venv venv
	venv/bin/pip install -e .[test]

export ANSIBLE_COLLECTIONS_PATH = $(shell pwd)/ansible_collections

ansible_collections: venv
	venv/bin/ansible-galaxy collection install -r requirements.yml

test: venv
	venv/bin/pytest tests/functional tests/unit

integration: venv ansible_collections
	venv/bin/pytest tests/integration

clean:
	git clean -xdf
