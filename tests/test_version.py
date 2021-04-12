"""
Test that the version number exists and that it is valid.
"""
import packaging

import ertai


def test_version_is_str():
    """Test that version is a string."""
    assert type(ertai.__version__) is str


def test_version_valid():
    """
    Test that version is of correct form.

    This allows things like 3.4.0beta.
    """
    assert type(packaging.version.parse(ertai.__version__)) is packaging.version.Version
