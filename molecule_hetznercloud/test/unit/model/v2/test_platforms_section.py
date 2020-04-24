import pytest
from molecule.model import schema_v3


@pytest.fixture
def _model_platform_hetznercloud_section_data():
    return {
        "driver": {"name": "hetznercloud"},
        "platforms": [
            {
                "name": "instance",
                "server_type": "",
                "volumes": [""],
                "image": "",
                "location": "",
                "datacenter": "",
                "user_data": "",
            }
        ],
    }


@pytest.mark.parametrize(
    "_config", ["_model_platform_hetznercloud_section_data"], indirect=True
)
def test_platforms_hetznercloud(_config):
    assert {} == schema_v3.validate(_config)


@pytest.fixture
def _model_platforms_hetznercloud_errors_section_data():
    return {
        "driver": {"name": "hetznercloud"},
        "platforms": [
            {
                "name": 0,
                "server_type": 0,
                "volumes": {},
                "image": 0,
                "location": 0,
                "datacenter": 0,
                "user_data": 0,
            }
        ],
    }


@pytest.mark.skip(reason="https://github.com/ansible/molecule/issues/2442")
@pytest.mark.parametrize(
    "_config", ["_model_platforms_hetznercloud_errors_section_data"], indirect=True
)
def test_platforms_hetznercloud_has_errors(_config):
    expected_config = {
        "platforms": [
            {
                0: [
                    {
                        "name": ["must be of string type"],
                        "server_type": ["must be of string type"],
                        "volumes": ["must be of list type"],
                        "image": ["must be of string type"],
                        "location": ["must be of string type"],
                        "datacenter": ["must be of string type"],
                        "user_data": ["must be of string type"],
                    }
                ]
            }
        ]
    }

    assert expected_config == schema_v3.validate(_config)


@pytest.mark.skip(reason="https://github.com/ansible/molecule/issues/2442")
@pytest.mark.parametrize(
    "_config", ["_model_platform_hetznercloud_section_data"], indirect=True
)
@pytest.mark.parametrize("_required_field", ("server_type", "image"))
def test_platforms_hetznercloud_fields_required(_config, _required_field):
    del _config["platforms"][0][_required_field]
    expected_config = {"platforms": [{0: [{_required_field: ["required field"]}]}]}
    assert expected_config == schema_v3.validate(_config)
