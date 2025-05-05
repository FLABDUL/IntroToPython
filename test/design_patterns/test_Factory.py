import unittest

from src.design_patterns.Factory import AnimalFactory


class TestFactory(unittest.TestCase):
    def test_create_dog(self):
        dog = AnimalFactory.create_animal("dog")
        self.assertEqual(dog.speak(), "Woof!")

    def test_create_cat(self):
        cat = AnimalFactory.create_animal("cat")
        self.assertEqual(cat.speak(), "Meow!")

    def test_invalid_animal(self):
        with self.assertRaises(ValueError):
            AnimalFactory.create_animal("bird")
