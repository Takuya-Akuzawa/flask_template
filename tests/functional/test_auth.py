"""
This file (test_users.py) contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `auth` blueprint.
"""


def test_profile(test_client):
    response = test_client.get('/profile')
    assert response.status_code == 200
    assert b'Logged in User Page' in response.data


def test_register(test_client):
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b'User Registration' in response.data


def test_login(test_client):
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'login' in response.data

def test_login_already_exists(test_client):
    response = test_client.post('login')
    assert response.status_code == 200
    assert b'already exists' in response.data



def test_logout(test_client):
    response = test_client.get('/logout')
    assert response.status_code == 200
    assert b'logout' in response.data