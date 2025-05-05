class CleanPythonicCode:
    def descriptive_names(self, value):
        # 🚫 Not Pythonic
        # def f(a):
        #     return a * 2

        # ✅ Pythonic
        return value * 2  # Clear intent using good naming

    def list_comprehension_example(self):
        # 🚫 Not Pythonic
        squares = []
        for x in range(10):
            squares.append(x * x)

        # ✅ Pythonic
        squares = [x * x for x in range(10)]
        return squares

    def boolean_expression(self, is_admin):
        # 🚫 Not Pythonic
        # if is_admin == True:
        #     grant_access()

        # ✅ Pythonic
        return "Access granted" if is_admin else "Access denied"

    def unpacking_example(self):
        my_tuple = (10, 20)

        # 🚫 Not Pythonic
        # x = my_tuple[0]
        # y = my_tuple[1]

        # ✅ Pythonic
        x, y = my_tuple
        return x + y

    def eafp_vs_lbyl(self, my_dict):
        # 🚫 Not Pythonic (LBYL - Look Before You Leap)
        if "key" in my_dict:
            value = my_dict["key"]
        else:
            value = "default"

        # ✅ Pythonic (EAFP - Easier to Ask Forgiveness than Permission)
        try:
            value = my_dict["key"]
        except KeyError:
            value = "default"

        return value

    def generator_vs_list(self, items):
        def process(x):
            return x * 2

        # 🚫 Not Pythonic
        results = [process(x) for x in items]
        result_sum_list = sum(results)

        # ✅ Pythonic (use generator expression)
        result_sum_gen = sum(process(x) for x in items)

        return result_sum_list, result_sum_gen

    def standard_library_use(self, n):
        # 🚫 Not Pythonic (reinventing the wheel)
        def manual_factorial(n):
            result = 1
            for i in range(2, n+1):
                result *= i
            return result

        # ✅ Pythonic
        import math
        return math.factorial(n)

    def context_manager(self, filename):
        # 🚫 Not Pythonic
        try:
            f = open(filename)
            data = f.read()
        finally:
            f.close()

        # ✅ Pythonic
        with open(filename) as f:
            data = f.read()

        return data

    def expressive_vs_dense_one_liner(self):
        # ✅ This is okay if simple:
        return [x ** 2 for x in range(10) if x % 2 == 0]

        # 🚫 Don't do this:
        # print([x**2 for x in range(10) if x % 2 == 0 and x > 3 and some_other_condition(x)])

# Example Usage
if __name__ == "__main__":
    cpc = CleanPythonicCode()
    print("Double of 5:", cpc.descriptive_names(5))
    print("Squares:", cpc.list_comprehension_example())
    print("Boolean test (admin):", cpc.boolean_expression(True))
    print("Tuple unpacking result:", cpc.unpacking_example())
    print("Dict lookup result:", cpc.eafp_vs_lbyl({'another_key': 5}))
    print("Generator vs List Sum:", cpc.generator_vs_list([1, 2, 3]))
    print("Factorial of 5:", cpc.standard_library_use(5))
    print("Expressive one-liner:", cpc.expressive_vs_dense_one_liner())
