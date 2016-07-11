#coding:utf8

'''
handle the errors with blueprint

in the blueprint handler,if you wish using @errorhandler,
you'd better write like this:@main.app_errorhandler,
so,the error handler will take the whole app's error.# 全局处理变量
'''

from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

