# coding:utf8

from flask import Blueprint

auth = Blueprint('auth', __name__)  # create blueprint namespace 'auth'

from . import views     # import route


