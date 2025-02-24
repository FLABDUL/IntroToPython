import sys

class GettingStartedDemo:
    def __init__(self):
        self.name = "Alice"
        self.age = 30
        self.height = 5.6  # height in feet

    def using_variables(self):
        """Demonstrates using variables."""
        print(f"Using Variables:")
        print(f"Name: {self.name}, Age: {self.age}, Height: {self.height} feet\n")

    def builtin_functions(self):
        """Demonstrates some built-in functions."""
        print("Using Built-in Functions:")
        numbers = [1, 2, 3, 4, 5]
        print(f"Sum of numbers: {sum(numbers)}")
        print(f"Maximum number: {max(numbers)}")
        print(f"Minimum number: {min(numbers)}\n")

    def strings(self):
        """Demonstrates string operations."""
        print("Working with Strings:")
        greeting = f"Hello, {self.name}!"
        print(greeting)
        print(f"Length of the greeting: {len(greeting)} characters\n")

    def numbers(self):
        """Demonstrates working with numbers."""
        print("Working with Numbers:")
        num1 = 10
        num2 = 3
        print(f"Addition: {num1} + {num2} = {num1 + num2}")
        print(f"Division: {num1} / {num2} = {num1 / num2}")
        print(f"Integer Division: {num1} // {num2} = {num1 // num2}")#/ is fp a // is int
        print(f"Power: {num1} ** 2 = {num1 ** 2}\n")

    def converting_types(self):
        """Demonstrates type conversion."""
        print("Converting Among Types:")
        str_number = "123"
        int_number = int(str_number)
        float_number = float(str_number)
        print(f"String '{str_number}' converted to Integer: {int_number}")
        print(f"String '{str_number}' converted to Float: {float_number}\n")

    def writing_to_screen(self):
        """Demonstrates writing to the screen."""
        print("Writing to the Screen:")
        print("This is an example of writing output to the console.\n")

    def command_line_parameters(self):
        """Demonstrates handling command line parameters."""
        print("Command Line Parameters:")
        if len(sys.argv) > 1:#first element is name of script e.g. python my_script.py arg1 arg2 arg3
            print("Command line arguments received:")
            for arg in sys.argv[1:]:
                print(f" - {arg}")
        else:
            print("No command line arguments received.\n")

    def run_demo(self):
        """Runs all demonstration methods."""
        self.using_variables()
        self.builtin_functions()
        self.strings()
        self.numbers()
        self.converting_types()
        self.writing_to_screen()
        self.command_line_parameters()

# Create an instance of the demo class
demo = GettingStartedDemo()

# Run the demonstration
demo.run_demo()
