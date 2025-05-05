import unittest

from src.Icp import Dog, Cat, Animal, animal_sound, Car


class TestOOPPrinciples(unittest.TestCase):

    # === Inheritance Tests ===
    def test_inheritance_dog(self):
        dog = Dog()
        self.assertEqual(dog.speak(), "Woof!")  # Dog overrides speak()

    def test_inheritance_cat(self):
        cat = Cat()
        self.assertEqual(cat.speak(), "Meow!")  # Cat overrides speak()

    def test_inheritance_base_class(self):
        animal = Animal()
        self.assertEqual(animal.speak(), "Some sound")  # Base implementation

    # === Polymorphism Tests ===
    def test_polymorphism_dog(self):
        self.assertEqual(animal_sound(Dog()), "Woof!")  # Same function, different behavior

    def test_polymorphism_cat(self):
        self.assertEqual(animal_sound(Cat()), "Meow!")  # Same function, different behavior

    # === Composition Tests ===
    def test_composition_car_starts_engine(self):
        car = Car()
        self.assertEqual(car.start(), "Engine starting...")  # Car uses Engine internally

if __name__ == "__main__":
    unittest.main()
