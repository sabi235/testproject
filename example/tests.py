from django.test import TestCase
import unittest


class DummyTest(TestCase):

    def test_dummy(self):
        self.assertEqual(True, True)


class TestStringMethods(unittest.TestCase):
z
        def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')
