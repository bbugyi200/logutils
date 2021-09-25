"""Tests the logutils.cli module."""

from logutils.cli import main


def test_main() -> None:
    """Tests main() function."""
    assert main([""]) == 0
