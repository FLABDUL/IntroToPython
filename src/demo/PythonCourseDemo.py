# 1. Basic Syntax & Variables
class BasicSyntax:
    def __init__(self):#constructor
        self.message = "Hello, Python!"

    def display_message(self):
        print(self.message)


# 2. Flow Control
class FlowControl:
    def check_number(self, num):#self is the calling class
        if num > 0:
            print("Positive number")
        elif num < 0:
            print("Negative number")
        else:
            print("Zero")

    def loop_example(self):
        for i in range(5):
            print(f"Loop iteration: {i}")


# 3. Sequences (Lists, Tuples)
class Sequences:
    def list_demo(self):
        my_list = [1, 2, 3, 4]
        print("List: ", my_list)
        my_list.append(5)
        print("Updated List: ", my_list)

    def tuple_demo(self):
        my_tuple = (10, 20, 30)
        print("Tuple: ", my_tuple)


# 4. File Handling
class FileHandling:
    def write_file(self):
        with open("example.txt", "w") as file:#w/r is mode write/read
            file.write("Hello, File!")

    def read_file(self):
        with open("example.txt", "r") as file:
            content = file.read()
            print("File Content: ", content)


# 5. Dictionaries & Sets
class DictionariesSets:
    def dict_demo(self):
        my_dict = {"name": "Alice", "age": 25}#any hashable datat type can be used in dict
        print("Dictionary: ", my_dict)

    def set_demo(self):
        my_set = {1, 2, 3, 3}
        print("Set: ", my_set)


# 6. Functions
class FunctionsDemo:
    def add_numbers(self, a, b):
        return a + b


# 7. Sorting
class SortingDemo:
    def sort_list(self):
        numbers = [4, 2, 9, 1]
        print("Sorted List: ", sorted(numbers))#can sort any iterable type


# 8. Error Handling
class ErrorHandling:
    def safe_divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:#choose error based on expected
            result = "Cannot divide by zero"
        print("Result: ", result)


# 9. Modules & Packages
import math


class ModulesDemo:
    def use_math_module(self):
        print("Square root of 16: ", math.sqrt(16))


# 10. Regular Expressions
import re


class RegexDemo:
    def find_pattern(self, text):
        match = re.search(r"\d+", text)
        print("Found number: ", match.group() if match else "No match")


# 11. Standard Library
import random


class StandardLibraryDemo:
    def generate_random(self):
        print("Random Number: ", random.randint(1, 100))


# 12. Object-Oriented Programming (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


# Running Demonstrations
if __name__ == "__main__":
    print("--- Basic Syntax ---")
    basic = BasicSyntax()
    basic.display_message()

    print("\n--- Flow Control ---")
    flow = FlowControl()
    flow.check_number(10)#flow is passed in as self, same as Flow.check_number(flow, 10)
    flow.loop_example()

    print("\n--- Sequences ---")
    seq = Sequences()
    seq.list_demo()#mutable, need modify/add/remove
    seq.tuple_demo()#immutable, use as dict key since hashable

    print("\n--- File Handling ---")
    file_demo = FileHandling()
    file_demo.write_file()
    file_demo.read_file()

    print("\n--- Dictionaries & Sets ---")
    ds = DictionariesSets()
    ds.dict_demo()
    ds.set_demo()

    print("\n--- Functions ---")
    func = FunctionsDemo()
    print("Sum: ", func.add_numbers(5, 3))

    print("\n--- Sorting ---")
    sort_demo = SortingDemo()
    sort_demo.sort_list()

    print("\n--- Error Handling ---")
    err = ErrorHandling()
    err.safe_divide(10, 0)

    print("\n--- Modules & Packages ---")
    mod = ModulesDemo()
    mod.use_math_module()

    print("\n--- Regular Expressions ---")
    regex = RegexDemo()
    regex.find_pattern("The price is 100 dollars.")

    print("\n--- Standard Library ---")
    std_lib = StandardLibraryDemo()
    std_lib.generate_random()

    print("\n--- Object-Oriented Programming ---")
    person = Person("John", 30)
    person.introduce()
