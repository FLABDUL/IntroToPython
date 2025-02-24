class DictSetDemo:
    def __init__(self):
        # Creating a dictionary
        self.my_dict = {"name": "Alice", "age": 25, "city": "New York"}
        # Creating a set
        self.my_set = {1, 2, 3, 4, 5}

    def iterate_dictionary(self):
        """Iterates through dictionary and prints key-value pairs."""
        for key, value in self.my_dict.items():
            print(f"{key}: {value}")

    def add_to_dict(self, key, value):
        """Adds a key-value pair to the dictionary."""
        self.my_dict[key] = value

    def remove_from_dict(self, key):
        """Removes a key from the dictionary if it exists."""
        if key in self.my_dict:
            del self.my_dict[key]

    def add_to_set(self, value):
        """Adds an element to the set."""
        self.my_set.add(value)

    def remove_from_set(self, value):
        """Removes an element from the set if it exists."""
        self.my_set.discard(value)  # discard() avoids error if value is not in set

    def display_set(self):
        """Displays all elements in the set."""
        print("Set Elements:", self.my_set)

    def set_operations(self, another_set):
        """Performs union, intersection, and difference operations."""
        print("Union:", self.my_set | another_set)
        print("Intersection:", self.my_set & another_set)
        print("Difference:", self.my_set - another_set)


# Example usage
if __name__ == "__main__":
    demo = DictSetDemo()

    # Dictionary operations
    print("Dictionary:")
    demo.iterate_dictionary()
    demo.add_to_dict("country", "USA")
    print("After Adding:", demo.my_dict)
    demo.remove_from_dict("age")
    print("After Removing Age:", demo.my_dict)

    # Set operations
    print("\nSet:")
    demo.display_set()
    demo.add_to_set(6)
    print("After Adding 6:", demo.my_set)
    demo.remove_from_set(2)
    print("After Removing 2:", demo.my_set)

    # Set operations with another set
    another_set = {3, 4, 5, 6, 7}
    print("\nSet Operations:")
    demo.set_operations(another_set)
