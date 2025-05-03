class FlowControlDemo:
    def __init__(self):
        self.number = 5  # Example number to demonstrate flow control

    def about_flow_control(self):
        """Demonstrates the importance of flow control."""
        print("Flow control refers to the order in which individual statements, "
              "instructions, or function calls are executed or evaluated in a program.")
        print("Using flow control structures (like if statements, loops, etc.) "
              "allows you to dictate the execution path based on certain conditions.\n")

    def demonstrate_whitespace(self):
        """Demonstrates the significance of whitespace in Python."""
        print("In Python, whitespace is crucial for defining the structure of the code.")
        print("Indentation determines the grouping of statements (like in functions, loops, etc.).")
        print("For example, the following code block is only executed if the condition is true:\n")
        print("if self.number > 3:")
        print("    print('Number is greater than 3')")
        print("The indented print statement belongs to the if statement.\n")

    def conditional_expressions(self):
        """Demonstrates conditional expressions."""
        print("Conditional Expressions:")
        result = "Even" if self.number % 2 == 0 else "Odd"
        print(f"The number {self.number} is {result}.\n")

    def relational_and_boolean_operators(self):
        """Demonstrates relational and Boolean operators."""
        print("Relational and Boolean Operators:")
        a = 10
        b = 5
        print(f"a = {a}, b = {b}")
        print(f"a > b: {a > b}")   # True
        print(f"a < b: {a < b}")   # False
        print(f"a == b: {a == b}")  # False
        print(f"a != b: {a != b}")  # True
        print(f"a >= b: {a >= b}")  # True
        print(f"a <= b: {a <= b}\n")  # False

        # Boolean operators
        print(f"(a > b) and (b > 0): {(a > b) and (b > 0)}")  # True
        print(f"(a < b) or (b > 0): {(a < b) or (b > 0)}")    # True
        print(f"not (a == b): {not (a == b)}\n")              # True

    def while_loops(self):
        """Demonstrates the use of while loops."""
        print("While Loops:")
        count = 0
        print("Counting to 5:")
        while count < 5:#prints 5 since increment happens inside while
            count += 1
            print(f"Count: {count}")
        print("Done counting!\n")

    def alternate_loop_exits(self):
        """Demonstrates alternate loop exits using break and continue."""
        print("Alternate Loop Exits:")
        print("Using 'break' and 'continue' in a while loop:")
        count = 0

        while count < 10:
            count += 1
            if count == 3:
                print("Skipping 3 (using continue)")
                continue  # Skip the rest of the loop for count == 3
            if count == 8:
                print("Breaking the loop at count == 8")
                break  # Exit the loop when count == 8
            print(f"Count: {count}")
        print("Loop ended.\n")

    def run_demo(self):
        """Runs all demonstration methods."""
        self.about_flow_control()
        self.demonstrate_whitespace()
        self.conditional_expressions()
        self.relational_and_boolean_operators()
        self.while_loops()
        self.alternate_loop_exits()

# Create an instance of the demo class
demo = FlowControlDemo()

# Run the demonstration
demo.run_demo()
