#coding:utf8

'''
support the templates form require
'''

from flask_wtf import Form
from wtforms import StringField, SubmitField \
    # get the text data and commit button data .
from wtforms.validators import Required \
    # Required validata the data is not null


class NameForm(Form):
    # name 是一个文本字段 变量,具体表示为type='text'的<input>元素
    name = StringField('What is your name?', validators=[Required()])
    # SubmitField is > type="submit"的,<input>元素
    submit = SubmitField('Submit')
