from __future__ import annotations

from molecule import api


def test_driver_is_detected():
    assert "molecule_hetznercloud" in [str(d) for d in api.drivers()]
