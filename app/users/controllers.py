# -*- coding: utf-8 -*-
from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required

from . import user
from .. import db
from models import User


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

@user.route('/users')
@login_required
def list_users():
    """
    List all users ordered by latest
    """
    check_admin()
    results = User.query.order_by(-User.id)
    return render_template('user_list.html', users=results)


@user.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    """
    load form page and add to the database
    """
    check_admin()

    # if form submit
    if request.method == 'POST':
        #  create new user with UI form data
        user = User(username=request.form['username'],
                    password=request.form['password'],
                    is_admin=request.form.getlist('is_admin'))

        try:
            # add user to the database
            db.session.add(user)
            db.session.commit()
            # message to the UI
            flash('Utilizador adicionado com sucesso.', 'success')
            # redirect to the users page
            return redirect(url_for('user.list_users'))
        except:
            # in case user name already exists
            flash('Erro: username já existe.', 'danger')
            return redirect(url_for('user.add_user'))

    # load add user form template
    return render_template('user_add.html')


@user.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    check_admin()

    # get user or error
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        # update user with UI form data
        user.username = request.form['username']
        user.password = request.form['password']
        user.is_admin = request.form.getlist('is_admin')
        # update user in database
        db.session.commit()
        # message to the UI
        flash('Utilizador alterado com sucesso.', 'success')

        # redirect to the users page
        return redirect(url_for('user.list_users'))

    return render_template('user_edit.html', user=user)


@user.route('/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    """
    Delete from database
    """
    check_admin()

    # get user or error
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Utilizador removido com sucesso.', 'success')

    # redirect to the users page
    return redirect(url_for('user.list_users'))
