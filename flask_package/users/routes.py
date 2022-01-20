#################
#### imports ####
#################
from flask import render_template, request, flash, redirect, url_for

from . import users_blueprint
from flask_package.models import User
from flask_package import db

#################
#### routes ####
#################

@users_blueprint.route('/profile')
def profile():
    return render_template('profile.html')