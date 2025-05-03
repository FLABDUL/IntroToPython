import time


# A simple decorator to log the function call
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function: {func.__name__} returned: {result}")
        return result

    return wrapper


# A decorator to measure the execution time of a function
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result

    return wrapper


# A decorator that modifies the result of a function
def modify_result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        modified_result = f"Modified: {result}"
        return modified_result

    return wrapper


# The class that uses decorators
class DecoratorDemo:

    @log_decorator  # Apply the logging decorator
    @time_decorator  # Apply the timing decorator
    def add(self, a, b):
        return a + b

    @modify_result_decorator  # Apply the result modification decorator
    def greet(self, name):
        return f"Hello, {name}!"

    def run(self):
        # Calling decorated functions
        print(self.add(3, 4))  # This will call both time_decorator and log_decorator
        print(self.greet("John"))  # This will call modify_result_decorator


if __name__ == "__main__":
    demo = DecoratorDemo()
    demo.run()
