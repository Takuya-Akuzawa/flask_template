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
            user = User('test_user@gmail.com', 'test_user', 'aaaa')
            db.session.add(user)
            db.session.commit()

            yield testing_client  # this is where the testing happens!

            user = User.query.filter_by(email='test_user@gmail.com').first()
            db.session.delete(user)
            db.session.commit()


@pytest.fixture(scope='module')
def new_user():
    user = User('test_user@gmail.com', 'test_user', 'Passw0rd')
    return user


