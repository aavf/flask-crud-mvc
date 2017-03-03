# -*- coding: utf-8 -*-
from .. import db


class Person(db.Model):
    """
    Create a Person table
    """

    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    birthdate = db.Column(db.DateTime)
    gender = db.Column(db.String(60))
    phone = db.Column(db.String(60))
    email = db.Column(db.String(60))
    address = db.Column(db.Text)
    profession = db.Column(db.String(60))
    marital_status = db.Column(db.String(60))

    def __repr__(self):
        return '<Person %r %r>' % (self.first_name, self.last_name)
