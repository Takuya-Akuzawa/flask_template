"""
This file (test_users.py) contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `users` blueprint.
"""


def test_profile(test_client):
    response = test_client.get('/profile')
    assert b'Logged in User Page' in response.data
    assert response.status_code == 200
