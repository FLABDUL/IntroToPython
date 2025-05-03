class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):  # Violates LSP
    def fly(self):
        raise Exception("Ostriches can't fly!")

class BirdLsp:
    pass

class FlyingBird(BirdLsp):
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(BirdLsp):
    pass
