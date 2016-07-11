#coding:utf8

'''
this is a unittest demo,
it is just a simply testing program
have fun
'''

import unittest

from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):        # create a new test config env and db
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):       # testing whether the instance exist
        self.assertFalse(current_app is None)

    def test_app_testing(self):     # testing whether the config running
        self.assertTrue(current_app.config['TESTING'])

