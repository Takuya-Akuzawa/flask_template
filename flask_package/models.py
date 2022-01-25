from flask_package import db

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model): # type: ignore
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        * email - email address of the user
        * user_name - registered user name
        * hashed password - hashed password (using werkzeug.security)
        * registered_date - date & time that the user registered

    REMEMBER: Never store the plaintext password in a database!
    """

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # type: ignore
    email = db.Column(db.String, unique=True, nullable=False) # type: ignore
    user_name = db.Column(db.String(32), nullable=False) # type: ignore
    hashed_password = db.Column(db.String(128), nullable=False) # type: ignore
    registered_date = db.Column(db.DateTime, nullable=False) # type: ignore

    def __init__(self, email: str, user_name: str, password_plaintext: str):
        """
        Create a new User object using the email and hashing the plaintext password
        using Werkzeug.Security.
        """
        self.email = email
        self.user_name = user_name
        self.hashed_password = self._generate_password_hash(password_plaintext)
        self.registered_date = datetime.now()

    def __repr__(self):
        return f'<User: {self.user_name}, {self.email}>'

    @staticmethod
    def _generate_password_hash(password_plaintext: str):
        return generate_password_hash(password_plaintext)
                
    def set_password(self, password_plaintext: str):
        self.hashed_password = self._generate_password_hash(password_plaintext)
    
    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.hashed_password, password_plaintext)

    def get_id(self):
        """Return the user ID as a Unicode string(`str`)."""
        return str(self.id)

    @property
    def is_authenticated(self):
        """Return True if the user has been successfully registered."""
        return True

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

