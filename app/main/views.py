#coding:utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main  #import blueprint
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        #
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())

@main.route('/info')
def info():
    return render_template('info.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/faq')
def faq():
    return render_template('faq.html')