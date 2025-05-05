class PythonicExamples:
    def swap_values(self, a, b):
        # 🚫 Non-Pythonic
        temp = a
        a = b
        b = temp

        # ✅ Pythonic
        a, b = b, a
        return a, b

    def loop_with_index(self, my_list):
        # 🚫 Non-Pythonic
        for i in range(len(my_list)):
            print(i, my_list[i])

        # ✅ Pythonic
        for index, value in enumerate(my_list):
            print(index, value)

    def join_strings(self, words):
        # 🚫 Non-Pythonic
        sentence = ""
        for word in words:
            sentence += word + " "
        sentence = sentence.strip()

        # ✅ Pythonic
        sentence = " ".join(words)
        return sentence

    def list_comprehension(self):
        # 🚫 Non-Pythonic
        squares = []
        for x in range(10):
            squares.append(x * x)

        # ✅ Pythonic
        squares = [x * x for x in range(10)]
        return squares

    def check_empty(self, my_list):
        # 🚫 Non-Pythonic
        if len(my_list) == 0:
            return "Empty"

        # ✅ Pythonic
        if not my_list:
            return "Empty"

        return "Not Empty"

    def read_file(self, filename):
        # 🚫 Non-Pythonic
        f = open(filename)
        try:
            contents = f.read()
        finally:
            f.close()

        # ✅ Pythonic
        with open(filename) as f:
            contents = f.read()

        return contents

    def dict_get(self, my_dict, key, default_value):
        # 🚫 Non-Pythonic
        if key in my_dict:
            value = my_dict[key]
        else:
            value = default_value

        # ✅ Pythonic
        value = my_dict.get(key, default_value)
        return value

    def any_example(self, numbers):
        # 🚫 Non-Pythonic
        found = False
        for x in numbers:
            if x > 10:
                found = True
                break
        if found:
            return "Some numbers > 10"

        # ✅ Pythonic
        if any(x > 10 for x in numbers):
            return "Some numbers > 10"

        return "All numbers ≤ 10"
