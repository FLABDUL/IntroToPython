class FunctionDemo:
    global_variable = "I am global"

    def simple_function(self):
        """Defines a basic function."""
        print("Hello from a simple function!")

    def function_with_parameters(self, name, age):
        """Defines a function with parameters."""
        print(f"Name: {name}, Age: {age}")

    def function_with_scope(self):
        """Demonstrates local and global scope."""
        local_variable = "I am local"
        print("Inside function, local_variable:", local_variable)
        print("Inside function, global_variable:", self.global_variable)

    def function_with_nested(self):
        """Demonstrates a nested function."""

        def nested_function():
            print("Hello from nested function!")

        nested_function()  # Calling the nested function

    def function_with_return(self, a, b):
        """Defines a function that returns a value."""
        return a + b


# Example usage
if __name__ == "__main__":
    demo = FunctionDemo()

    # Simple function
    demo.simple_function()

    # Function with parameters
    demo.function_with_parameters("Alice", 25)

    # Function demonstrating scope
    demo.function_with_scope()

    # Function with nested function
    demo.function_with_nested()

    # Function with return value
    result = demo.function_with_return(10, 20)
    print("Returned Value:", result)
