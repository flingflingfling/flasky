# coding:utf8

import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='ohh')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='ohh')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='ohh')
        self.assertTrue(u.verify_password('ohh'))
        self.assertFalse(u.verufy_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='ohh')
        u2 = User(password='doge')
        self.assertTrue(u.password_hash != u2.password_hash)
