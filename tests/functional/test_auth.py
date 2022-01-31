"""
This file (test_users.py) contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `auth` blueprint.
"""

from flask_login import current_user
from flask_package import db
from flask_package.models import User


def test_login_to_logout(test_client, init_database):
    """
    GIVEN a existing user
    WHEN access to login page and login with valid keys, then logout
    THEN check the login page is returned and successfully login, then, successfully logout
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'login' in response.data

    response = test_client.post('/login',
                                data={'email': 'test_user@gmail.com','password': 'aaaa'},
                                follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    assert b"Logged in User" in response.data
    assert current_user.is_authenticated # type: ignore

    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Logged out' in response.data
    assert not current_user.is_authenticated # type: ignore


def test_profile_not_logged_in(test_client, init_database):
    """
    GIVEN
    WHEN requested profile page with no login
    THEN check a message returned that prompts for login
    """
    
    response = test_client.get('/profile', follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    assert not current_user.is_authenticated # type: ignore
    assert b'Please log in' in response.data


def test_login_already_logged_in(test_client, init_database):
    """
    GIVEN a existing user
    WHEN once logged in, and request login page again
    THEN check that redirect to profile page and receive a message that tells already logged in
    """
    # setup
    test_client.post('/login',
                    data={'email': 'test_user@gmail.com','password': 'aaaa'},
                    follow_redirects=True)

    response = test_client.post('/login',
                                data={'email': 'test_user@gmail.com','password': 'aaaa'},
                                follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    assert b"Already logged in!" in response.data
    assert b'User Page' in response.data
    assert current_user.is_authenticated # type: ignore

    # Tear down
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Logged out' in response.data
    assert not current_user.is_authenticated # type: ignore


def test_invalid_login(test_client, init_database):
    """
    GIVEN 
    WHEN a login request with no existing user, or invalid login keys
    THEN check the login failed and receive a message that tells Login failed.
    """

    # attempt login with No existing user
    response = test_client.post('/login',
                                data={'email': 'no_user@gmail.com','password': 'xxxx'},
                                follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    assert b"Login failed" in response.data
    assert not current_user.is_authenticated # type: ignore
    
    # email validation error
    response = test_client.post('/login',
                                data={'email': 'no_user','password': 'xxxx'},
                                follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    assert b"Login failed" in response.data
    assert not current_user.is_authenticated # type: ignore


def test_valid_register(test_client, init_database):
    """
    GIVEN 
    WHEN access to register page and register with valid keys, then logout
    THEN check a new user registered and successfully login, then, successfully logout
    """
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b'User Registration' in response.data

    response = test_client.post('/register',
                                data=dict(
                                    email='new_user@gmail.com',
                                    user_name='new_user',
                                    password='newuserpass',
                                    confirm='newuserpass'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering' in response.data
    assert current_user.is_authenticated # type: ignore

    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Logged out' in response.data
    assert not current_user.is_authenticated # type: ignore

    # Tear down
    user = User.query.filter_by(email='new_user@gmail.com').first()
    db.session.delete(user)
    db.session.commit()


def test_invalid_register(test_client, init_database):
    """
    GIVEN 
    WHEN register a new user with invalid email
    THEN check the user is not be registered, and warning message is returned.
    """
    response = test_client.post('/register',
                                data=dict(
                                    email='invalid_gmail',
                                    user_name='invalid_user',
                                    password='invalidpass',
                                    confirm='invalidpass'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid email address' in response.data
    assert not current_user.is_authenticated # type: ignore


def test_register_page_already_login(test_client, init_database):
    """
    GIVEN a existing user
    WHEN once logged in, and request login page again
    THEN check that redirect to profile page and receive a message that tells already logged in
    """
    test_client.post('/register',
                    data=dict(
                        email='new_user@gmail.com',
                        user_name='new_user',
                        password='newuserpass',
                        confirm='newuserpass'),
                    follow_redirects=True)

    response = test_client.post('/register',
                                data=dict(
                                    email='new_user@gmail.com',
                                    user_name='new_user',
                                    password='newuserpass',
                                    confirm='newuserpass'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already registered' in response.data
    assert b'User Page' in response.data
    assert current_user.is_authenticated # type: ignore

    # Tear down
    user = User.query.filter_by(email='new_user@gmail.com').first()
    db.session.delete(user)
    db.session.commit()


def test_register_already_exists(test_client, init_database):
    """
    GIVEN a existing user
    WHEN register a new user using a already registered email
    THEN check the user is not be registered,
         redirected to Register page, and warning message is returned.
    """
    response = test_client.post('/register',
                            data=dict(
                                email='test_user@gmail.com',
                                user_name='duplicate_user',
                                password='duplicateuser',
                                confirm='duplicateuser'),
                            follow_redirects=True)
    assert response.status_code == 200
    assert b'User Registration' in response.data
    assert b'This email already exists' in response.data
    assert not current_user.is_authenticated # type: ignore