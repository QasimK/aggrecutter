import pytest

import web


def test_get_front_page_text():
    assert web.get_prefix().casefold().startswith("the")
