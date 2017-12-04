
import requests

BASE_URL = 'http://localhost:5000'

def test_get():
    "Check GET response sends 200"
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_put():
    "Check PUT response sends 405"
    response = requests.put(BASE_URL)
    assert response.status_code == 405

def test_delete():
    "Check DELETE response sends 405"
    response = requests.delete(BASE_URL)
    assert response.status_code == 405
