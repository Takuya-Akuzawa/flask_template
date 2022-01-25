"""
This file (test_users.py) contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `auth` blueprint.
"""


from dataclasses import dataclass


def test_profile(test_client):
    response = test_client.get('/profile')
    assert response.status_code == 200
    assert b'Logged in User Page' in response.data


def test_register_page(test_client):
    """
    GIVEN a existing user
    WHEN user request '/login' page
    THEN check the response is valid.
    """
    
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b'User Registration' in response.data


def test_register_valid_post(test_client):
    """
    GIVEN a existing user
    WHEN register a new user using a already registered email
    THEN check the user is not be registered, and warning message is returned.
    """
    response = test_client.post('/register',
                    data=dict(
                        email='test_user@gmail.com',
                        user_name='test_user',
                        password='aaaa',
                        confirm='aaaa'),
                    follow_redirects=True)
    assert response.status_code == 200
    # assert b'Thanks for registering' in response.data
    assert b'already exists' in response.data




def test_register_already_exists(test_client):
    """
    GIVEN a existing user
    WHEN register a new user using a already registered email
    THEN check the user is not be registered, and warning message is returned.
    """
    # test_client.post('/register',
    #                 data=dict(
    #                     email='test_user@gmail.com',
    #                     user_name='test_user',
    #                     password='aaaa',
    #                     confirm='aaaa'),
    #                     follow_redirects=True)

    response = test_client.post('/register',
                    data=dict(
                        email='test_user@gmail.com',
                        user_name='test_user',
                        password='aaaa',
                        confirm='aaaa'),
                    follow_redirects=True)
    assert response.status_code == 200
    assert b'User Registration' in response.data
    assert b'already exists' in response.data


def test_login(test_client):
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'login' in response.data

    response = test_client.post('login',
                                data={
                                    'email': 'test_user@gmail.com',
                                    'password': 'aaaa'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Logged in User" in response.data





def test_logout(test_client):
    response = test_client.get('/logout')
    assert response.status_code == 200
    assert b'logout' in response.data