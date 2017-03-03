# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required

from . import person
from .. import db
from models import Person


@person.route('/persons')
@login_required
def list_persons():
    """
    List all persons ordered by latest
    """
    persons = Person.query.order_by(-Person.id)
    return render_template('person_list.html',
                           persons=persons)

@person.route('/persons/add', methods=['GET', 'POST'])
@login_required
def add_person():
    """
    load form page and add to the database
    """
    # if form submit
    if request.method == 'POST':
        #  create new person with UI form data
        person = Person(first_name=request.form['first_name'],
                    last_name=request.form['last_name'],
                    birthdate=request.form['birthdate'],
                    gender=request.form['gender'],
                    phone=request.form['phone'],
                    email=request.form['email'],
                    address=request.form['address'],
                    profession=request.form['profession'],
                    marital_status=request.form['marital_status'])

        try:
            # add person to the database
            db.session.add(person)
            db.session.commit()
            # message to the UI
            flash('Pessoa adicionada com sucesso.', 'success')
        except:
            # in case person name already exists
            flash('Erro: ocorreu um erro desconhecido.', 'danger')

        # redirect to the persons list page
        return redirect(url_for('person.list_persons'))

    # load add person form template
    return render_template('person_add.html')


@person.route('/persons/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_person(id):
    # get person or error
    person = Person.query.get_or_404(id)

    if request.method == 'POST':
        # update person with UI form data
        person.first_name = request.form['first_name']
        person.last_name = request.form['last_name']
        person.birthdate = request.form['birthdate']
        person.gender = request.form['gender']
        person.phone = request.form['phone']
        person.email = request.form['email']
        person.address = request.form['address']
        person.profession = request.form['profession']
        person.marital_status = request.form['marital_status']
        db.session.commit()
        # message to the UI
        flash('Pessoa alterada com sucesso.', 'success')

        # redirect to the persons list page
        return redirect(url_for('person.list_persons'))

    return render_template('person_edit.html',
                           person=person)


@person.route('/persons/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_person(id):
    """
    Delete from database
    """
    # get person or error
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    flash('Pessoa removida com sucesso.', 'success')

    # redirect to list
    return redirect(url_for('person.list_persons'))
