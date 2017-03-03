from flask import Blueprint

person = Blueprint('person', __name__)

from . import controllers