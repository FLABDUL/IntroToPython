class PythonicToolsShowcase:
    def list_comprehension(self):
        # 🚫 Not Pythonic: building a list with a loop
        squares = []
        for x in range(5):
            squares.append(x ** 2)

        # ✅ Pythonic: use a list comprehension
        squares = [x ** 2 for x in range(5)]
        return squares

    def list_comprehension_with_condition(self):
        # ✅ Pythonic: filter and map in one line
        evens = [x for x in range(10) if x % 2 == 0]
        return evens

    def unpacking_example(self):
        point = (3, 4)

        # 🚫 Not Pythonic: using indexes
        x = point[0]
        y = point[1]

        # ✅ Pythonic: unpack directly
        x, y = point
        return x, y

    def unpacking_swap(self):
        a, b = 1, 2

        # ✅ Pythonic: swap with no temp variable
        a, b = b, a
        return a, b

    def zip_example(self):
        names = ["Alice", "Bob", "Charlie"]
        scores = [85, 90, 88]

        paired = []

        # 🚫 Not Pythonic: manual index access
        for i in range(len(names)):
            paired.append((names[i], scores[i]))

        # ✅ Pythonic: use zip for parallel iteration
        paired = [(name, score) for name, score in zip(names, scores)]
        return paired

    def enumerate_example(self):
        fruits = ["apple", "banana", "cherry"]

        result = []

        # 🚫 Not Pythonic: using range and index
        for i in range(len(fruits)):
            result.append((i, fruits[i]))

        # ✅ Pythonic: use enumerate
        result = [(index, fruit) for index, fruit in enumerate(fruits)]
        return result

    def nested_list_comprehension(self):
        # ✅ Pythonic: create 3x3 identity matrix
        identity_matrix = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
        return identity_matrix


# ✅ Example usage
if __name__ == "__main__":
    pts = PythonicToolsShowcase()

    print("List comprehension:", pts.list_comprehension())
    print("List comprehension with condition:", pts.list_comprehension_with_condition())
    print("Tuple unpacking:", pts.unpacking_example())
    print("Tuple unpacking (swap):", pts.unpacking_swap())
    print("Using zip():", pts.zip_example())
    print("Using enumerate():", pts.enumerate_example())
    print("Identity matrix (nested list comprehension):", pts.nested_list_comprehension())
