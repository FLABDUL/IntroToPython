class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):  # Robot shouldn't need eat()
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError()

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")
