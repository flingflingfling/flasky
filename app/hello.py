# coding:utf-8

import os
from flask import Flask, render_template, session, \
    redirect, url_for, flash
from flask_script import Manager, Shell     # add shell command support
from flask_bootstrap import Bootstrap
from flask_moment import Moment     # add localtime support
from datetime import datetime  # print the local time
from flask_wtf import Form
from wtforms import StringField, SubmitField \
    # get the text data and commit button data .
from wtforms.validators import Required \
    # Required validata the data is not null
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand   # add db-migration support
from flask_mail import Mail, Message



# initial app
app = Flask(__name__)

# database settings; using flask_sqlalchemy with mysql
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "sqlite:///" + os.path.join(basedir, 'flasky-sqlalchemy-sqlite3.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'do not you trust me '
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
migrate = Migrate(app, db)
mail = Mail(app)

# # mail config
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USR_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')   # get mail username and pw
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')   # from envronment
# app.config['FLASKY_MAIL_SUBJECT_PREFX'] = '[Flasky]'
# app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flask@flingfling.io>'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASK_MAILSUBJECT_PREFIX']) + subject,
                    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to]
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role',lazy='dynamic')
#     def __repr__(self):
#         return '<Role %r>' % self.name
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#     def __repr__(self):
#         return '<User %r>' % self.username


# view function
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))  # url_for must get 1
        # arguments, it is view function,here is index()
    return render_template('index.html', form=form, \
                name=session.get('name'), known = session.get('known',False),
                current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#
#
# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


# class NameForm(Form):
#     # name 是一个文本字段 变量,具体表示为type='text'的<input>元素
#     name = StringField('What is your name?', validators=[Required()])
#     # SubmitField is > type="submit"的,<input>元素
#     submit = SubmitField('Submit')

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)   # add db-migrate command

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
