import pytest
from flask_package import app
from flask_package.models.user import User


@pytest.fixture(scope='module')
def new_user():
    user = User('test_user@gmail.com', 'test_user', 'Passw0rd')
    return user
