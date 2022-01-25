"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from flask_package.models import User 


def test_new_user(new_user):
    """
    GIVEN a User Model
    WHEN a new User is created
    THEN check the email, password, registered_date
    """
    assert new_user.email == 'test_user@gmail.com'
    assert new_user.user_name == 'test_user'
    assert new_user.hashed_password != 'Passw0rd'
    assert new_user.__repr__() == '<User: test_user, test_user@gmail.com>'
    assert new_user.is_authenticated
    assert new_user.is_active
    assert not new_user.is_anonymous



def test_set_password(new_user):
    """
    GIVEN an existing User
    WHEN set a new password to the user
    THEN check the password is stored correctly, and not as plaintext
    """
    new_user.set_password('newPassword')
    assert new_user.hashed_password != 'newPassword'
    assert new_user.is_password_correct('newPassword')
    assert not new_user.is_password_correct('wrongPassword')


def test_get_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the ID is gained as String, not as Integer
    """
    new_user.id = 10
    assert new_user.get_id() == '10'
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)