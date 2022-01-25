"""
The views Blueprint handles the added application's business logics and routings.
Please add descriptions about your application.
"""
from flask import Blueprint
views_blueprint = Blueprint('views', __name__, template_folder='templates')

from . import routes
