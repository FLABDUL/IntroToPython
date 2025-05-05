from abc import ABC, abstractmethod

# ========== Inheritance ==========

class Animal:
    def speak(self):
        return "Some sound"

# Dog and Cat inherit from Animal and override speak()
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# ========== Polymorphism ==========

# Animal is the base class
# Any subclass of Animal can be used polymorphically
def animal_sound(animal: Animal):
    # This function works for any subclass of Animal
    return animal.speak()

# ========== Composition ==========

class Engine:
    def start(self):
        return "Engine starting..."

class Car:
    # Car 'has-a' Engine – this is composition
    def __init__(self):
        self.engine = Engine()

    def start(self):
        # Delegates work to the engine
        return self.engine.start()
