import unittest

from src.design_patterns.Singleton import Singleton


class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        a = Singleton()
        b = Singleton()
        self.assertIs(a, b)  # Both are the same instance
