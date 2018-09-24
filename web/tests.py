import pytest

from . import main


def test_get_front_page_text():
    assert main.get_prefix().casefold().startswith("the")
