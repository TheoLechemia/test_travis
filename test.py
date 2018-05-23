import pytest
import requests
from flask import url_for

from test_travis.app import get_app

@pytest.fixture
def app():
    app = get_app()
    return app

def test_first(client):
    print(dir(client))
    res = client.get(url_for('api.ping'))
    print(res)
    assert res.status_code == 200
    # resp = requests.get('http://127.0.0.1:5000/')
    # assert resp.status_code == 200