import os

import pytest
from molecule import util


@pytest.fixture
def _molecule_file():
    return os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        os.path.pardir,
        os.path.pardir,
        "resources",
        "molecule_hetznercloud.yml",
    )


@pytest.fixture
def _config(_molecule_file, request):
    d = util.safe_load(open(_molecule_file))
    if hasattr(request, "param"):
        d = util.merge_dicts(d, request.getfixturevalue(request.param))

    return d
