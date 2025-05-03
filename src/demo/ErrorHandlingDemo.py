class ErrorHandlingDemo:
    def demonstrate_syntax_error(self):
        print("\nDemonstrating Syntax Error (this line will be commented to avoid actual crash)")
        # Syntax errors can't actually be caught at runtime.
        # Example: Uncommenting the next line would cause a SyntaxError
        # eval('x === x')

    def demonstrate_exceptions(self):
        print("\nDemonstrating Exceptions")
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            print("Caught an exception:", e)

    def demonstrate_try_except_else_finally(self):
        print("\nDemonstrating try/except/else/finally")
        try:
            num = int(input("Enter a number: "))
            reciprocal = 1 / num
        except ValueError:
            print("That was not a valid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print("Reciprocal is:", reciprocal)
        finally:
            print("Execution completed (finally block).")

    def handle_multiple_exceptions(self):
        print("\nDemonstrating handling multiple exceptions")
        data = ['42', 'not_a_number', 0]
        for item in data:
            try:
                print("\nProcessing:", item)
                num = int(item)
                print("Reciprocal:", 1 / num)
            except (ValueError, ZeroDivisionError) as e:
                print("Caught an exception:", e)

    def ignore_exceptions(self):
        print("\nDemonstrating ignoring exceptions")
        try:
            risky_list = [1, 2, 3]
            print(risky_list[10])  # IndexError
        except IndexError:
            pass  # Silently ignore the error
        print("Program continues even after exception.")

if __name__ == "__main__":
    demo = ErrorHandlingDemo()
    demo.demonstrate_syntax_error()
    demo.demonstrate_exceptions()
    # Commented out the input section to prevent blocking in script runs
    # demo.demonstrate_try_except_else_finally()
    demo.handle_multiple_exceptions()
    demo.ignore_exceptions()
