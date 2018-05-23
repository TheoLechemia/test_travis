import pytest
import requests

def test_first():
    resp = requests.get('http://127.0.0.1:5000/')
    assert resp.status_code == 200