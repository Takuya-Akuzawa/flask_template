import pytest

from flask_package import create_app, db
from flask_package.models import User


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config['WTF_CSRF_ENABLED'] = False
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    """
    create a testing DB and testing user as setup
    when tests is finished, remove the testing DB as teardown
    """
    db.create_all()

    # create testing user
    user = User('test_user@gmail.com', 'test_user', 'aaaa')
    db.session.add(user)
    db.session.commit()
    
    yield # where tests starting

    db.drop_all()
