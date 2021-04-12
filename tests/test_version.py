"""
Test that the version number exists and that it is valid.
"""
import packaging

import ertai


def test_version_is_str():
    assert type(ertai.__version__) is str


def test_version_valid():
    assert type(packaging.version.parse(ertai.__version__)) is packaging.version.Version
