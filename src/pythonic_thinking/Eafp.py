class EAFPExamples:
    def dict_access(self, d):
        # 🚫 LBYL: check before access
        if 'name' in d:
            name = d['name']
        else:
            name = 'Unknown'

        # ✅ EAFP: try and handle exception
        try:
            name = d['name']
        except KeyError:
            name = 'Unknown'

        return name

    def attribute_access(self, obj):
        # 🚫 LBYL
        if hasattr(obj, 'id'):
            user_id = obj.id
        else:
            user_id = None

        # ✅ EAFP
        try:
            user_id = obj.id
        except AttributeError:
            user_id = None

        return user_id

    def file_read(self, filename):
        # ✅ EAFP with context manager
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "File not found."

    def division(self, a, b):
        # ✅ EAFP: handle division by zero
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero."

    def list_access(self, lst, index):
        # 🚫 LBYL
        if index < len(lst):
            value = lst[index]
        else:
            value = None

        # ✅ EAFP
        try:
            value = lst[index]
        except IndexError:
            value = None

        return value


# ✅ Example usage
if __name__ == "__main__":
    e = EAFPExamples()

    print("Dict access:", e.dict_access({"age": 30}))
    print("Attribute access:", e.attribute_access(type("User", (object,), {"id": 123})()))
    print("File read:", e.file_read("non_existent_file.txt"))
    print("Division:", e.division(10, 0))
    print("List index:", e.list_access([1, 2, 3], 5))
