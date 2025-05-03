from operator import itemgetter

class SortingDemo:
    @staticmethod
    def basic_sort():
        numbers = [5, 2, 9, 1, 5, 6]
        sorted_numbers = sorted(numbers)
        print("Basic sorted list:", sorted_numbers)

    @staticmethod
    def sort_with_alternate_keys():
        words = ['banana', 'pie', 'Washington', 'book']
        sorted_by_length = sorted(words, key=len)
        print("Sorted by length:", sorted_by_length)

    @staticmethod
    def sort_with_lambda():
        people = [
            {'name': 'John', 'age': 45},
            {'name': 'Diana', 'age': 30},
            {'name': 'Paul', 'age': 25}
        ]
        sorted_by_age = sorted(people, key=lambda person: person['age'])
        print("Sorted by age (lambda):", sorted_by_age)

    @staticmethod
    def sort_with_itemgetter():
        people = [
            ('John', 45),
            ('Diana', 30),
            ('Paul', 25)
        ]
        sorted_by_age = sorted(people, key=itemgetter(1))
        print("Sorted by age (itemgetter):", sorted_by_age)

    @staticmethod
    def reverse_sort():
        numbers = [5, 2, 9, 1, 5, 6]
        sorted_descending = sorted(numbers, reverse=True)
        print("Reverse sorted list:", sorted_descending)

    @staticmethod
    def multi_level_sort():
        people = [
            {'name': 'John', 'age': 45},
            {'name': 'Diana', 'age': 30},
            {'name': 'John', 'age': 25},
            {'name': 'Paul', 'age': 25}
        ]
        sorted_people = sorted(people, key=lambda person: (person['name'], person['age']))
        print("Multi-level sorted (by name, then age):", sorted_people)


if __name__ == "__main__":
    SortingDemo.basic_sort()
    SortingDemo.sort_with_alternate_keys()
    SortingDemo.sort_with_lambda()
    SortingDemo.sort_with_itemgetter()
    SortingDemo.reverse_sort()
    SortingDemo.multi_level_sort()
