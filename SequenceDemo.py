class SequenceDemo:
    def __init__(self):
        self.my_list = [1, 2, 3, 4, 5]  # Example list
        self.my_tuple = (10, 20, 30)  # Example tuple
        self.nested_list = [[1, 2], [3, 4], [5, 6]]  # Nested list

    def about_sequences(self):
        """About sequences in Python."""
        print("Sequences are ordered collections of items. They can contain elements of different types.")
        print("Common sequence types include lists, tuples, and strings.\n")

    def demonstrate_lists(self):
        """Demonstrates lists and list methods."""
        print("Lists:")
        print(f"Original List: {self.my_list}")

        # Adding an element
        self.my_list.append(6)
        print(f"After appending 6: {self.my_list}")

        # Removing an element
        self.my_list.remove(3)
        print(f"After removing 3: {self.my_list}")

        # Slicing the list
        sliced_list = self.my_list[1:4]  # Elements from index 1 to 3
        print(f"Sliced List (index 1 to 3): {sliced_list}")

        # List comprehension
        squared_list = [x ** 2 for x in self.my_list]
        print(f"Squared List (comprehension): {squared_list}\n")

    def demonstrate_tuples(self):
        """Demonstrates tuples."""
        print("Tuples:")
        print(f"Original Tuple: {self.my_tuple}")

        # Accessing tuple elements
        first_element = self.my_tuple[0]
        print(f"First element of tuple: {first_element}")

        # Attempting to modify a tuple will raise an error (tuples are immutable)
        print("Tuples are immutable; you cannot change their elements.\n")

    def indexing_and_slicing(self):
        """Demonstrates indexing and slicing."""
        print("Indexing and Slicing:")
        print(f"Original List: {self.my_list}")

        # Indexing
        print(f"Element at index 2: {self.my_list[2]}")

        # Slicing
        print(f"Elements from index 1 to 4: {self.my_list[1:4]}")
        print(f"Last two elements: {self.my_list[-2:]}\n")

    def iterating_through_sequences(self):
        """Demonstrates iterating through a sequence."""
        print("Iterating through List:")
        for item in self.my_list:
            print(f"Item: {item}")

        print("\nIterating through Tuple:")
        for item in self.my_tuple:
            print(f"Item: {item}")

        print("\nIterating through Nested List:")
        for sublist in self.nested_list:
            for item in sublist:
                print(f"Item in Nested List: {item}")
        print()#empty line for readability

    def sequence_functions_keywords_operators(self):
        """Demonstrates sequence functions, keywords, and operators."""
        print("Sequence Functions, Keywords, and Operators:")

        # Length of the list
        print(f"Length of the list: {len(self.my_list)}")

        # Checking membership
        print(f"Is 4 in the list? {'Yes' if 4 in self.my_list else 'No'}")

        # Concatenating lists
        new_list = self.my_list + [7, 8, 9]
        print(f"Concatenated List: {new_list}")

        # Repeating lists
        repeated_list = self.my_list * 2#copies list not multiplies elements
        print(f"Repeated List: {repeated_list}\n")

    def list_comprehensions(self):
        """Demonstrates list comprehensions."""
        print("List Comprehensions:")
        even_numbers = [x for x in range(10) if x % 2 == 0]
        print(f"Even numbers from 0 to 9: {even_numbers}\n")

    def generator_expressions(self):
        """Demonstrates generator expressions."""
        print("Generator Expressions:")
        squared_gen = (x ** 2 for x in range(5))  # Generator expression
        print("Squared numbers using generator expression:")
        for number in squared_gen:
            print(number)
        print()

    def nested_sequences(self):
        """Demonstrates nested sequences."""
        print("Nested Sequences:")
        print(f"Nested List: {self.nested_list}")
        print(f"Accessing element [1][0]: {self.nested_list[1][0]}")  # Accessing the element 3 from nested list
        print("Iterating through nested list:")
        for sublist in self.nested_list:
            print(f"Sublist: {sublist}")
            for item in sublist:
                print(f"Item: {item}")
        print()

    def run_demo(self):
        """Runs all demonstration methods."""
        self.about_sequences()
        self.demonstrate_lists()
        self.demonstrate_tuples()
        self.indexing_and_slicing()
        self.iterating_through_sequences()
        self.sequence_functions_keywords_operators()
        self.list_comprehensions()
        self.generator_expressions()
        self.nested_sequences()


# Create an instance of the demo class
demo = SequenceDemo()

# Run the demonstration
demo.run_demo()
