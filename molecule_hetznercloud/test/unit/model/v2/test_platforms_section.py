#  Copyright (c) 2015-2018 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import pytest

from molecule.model import schema_v2


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
    assert {} == schema_v2.validate(_config)


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

    assert expected_config == schema_v2.validate(_config)


@pytest.mark.parametrize(
    "_config", ["_model_platform_hetznercloud_section_data"], indirect=True
)
@pytest.mark.parametrize("_required_field", ("server_type", "image"))
def test_platforms_hetznercloud_fields_required(_config, _required_field):
    del _config["platforms"][0][_required_field]
    expected_config = {"platforms": [{0: [{_required_field: ["required field"]}]}]}
    assert expected_config == schema_v2.validate(_config)
