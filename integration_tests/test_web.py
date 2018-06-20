"""All integration tests."""

import requests


def test_front_page():
    # TODO: Env variable.
    response = requests.get("http://localhost:8080/")
    assert response.status_code == 200
