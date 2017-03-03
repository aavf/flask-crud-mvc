# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user

from . import auth
from .. import db
from ..users.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """
    # if form submit
    if request.method == 'POST':

        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(username=request.form['username']).first()
        if user is not None and user.verify_password(
                request.form['password']):
            # log employee in
            login_user(user)

            # redirect to certain page for admin or others users
            if user.is_admin:
                return redirect(url_for('user.list_users'))
            else:
                return redirect(url_for('person.list_persons'))

        # when login details are incorrect
        else:
            flash('Utilizador ou password inválido.', 'danger')

    # load login template
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an user out through the logout link
    """
    logout_user()
    flash('A sua sessão foi finalizada.', 'info')

    # redirect to the login page
    return redirect(url_for('auth.login'))
