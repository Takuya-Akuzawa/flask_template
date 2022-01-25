#################
#### imports ####
#################
from flask import render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, current_user, login_required, logout_user

from . import auth_blueprint
from .forms import LoginForm, RegisterForm
from flask_package.models import User
from flask_package import db

#################
#### routes ####
#################

@auth_blueprint.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    logger = current_app.logger
    if current_user.is_authenticated: # type: ignore
        flash('Already registered!  Redirecting to your User Profile page...', 'warning')
        return redirect(url_for('auth.profile'))

    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            logger.info('validate_on_submit = True')
            logger.info('a request to /register received.')
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                logger.info('inputted email is already registered.')
                flash(f'This email already exists', 'warning')
                return render_template('register.html', form=form)

            logger.info('START a new user registering')
            new_user = User(form.email.data, form.user_name.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()
            logger.info('SUCCESS a new user registering')
            login_user(new_user)
            flash(f'Thanks for registering, {new_user.user_name}', 'success')
            return redirect(url_for('auth.profile'))
        logger.info('validate_on_submit = False.')
    return render_template('register.html', form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    logger = current_app.logger
    if current_user.is_authenticated: # type: ignore
        flash('Already logged in!  Redirecting to your User Profile page...', 'warning')
        return redirect(url_for('auth.profile'))

    form = LoginForm()
    if request.method == 'POST':
        logger.info('a request to /login received.')
        if form.validate_on_submit():
            logger.info('validate_on_submit = True')
            
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.is_password_correct(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash(f'Thanks for logging in, {user.user_name}', 'success')
                return redirect(url_for('auth.profile'))
            logger.info('No user exists, or password is not correct')
        else:
            logger.info('validate_on_submit = False.')
        flash('Login failed. Please check your login details and try again', 'warning')
    return render_template('login.html', form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You are Logged out.')
    return redirect(url_for('auth.login'))