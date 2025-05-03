class CountUpTo:
    """
    An iterable class that counts from 1 up to a specified maximum number.
    It implements both __iter__ and __next__ methods.
    """
    def __init__(self, max_count):
        self.max_count = max_count  # The maximum number to count up to
        self.current = 1  # Start counting from 1

    def __iter__(self):
        """
        This method makes this class iterable.
        It returns the iterator object itself (usually self).
        """
        return self

    def __next__(self):
        """
        This method defines what happens when you call next() on the iterator.
        It raises StopIteration when the counting is finished.
        """
        if self.current <= self.max_count:
            num = self.current  # Store current number
            self.current += 1   # Move to next number
            return num
        else:
            # No more numbers left to iterate
            raise StopIteration


# Example usage
if __name__ == "__main__":
    counter = CountUpTo(5)  # Create an instance to count from 1 to 5

    print("Manual iteration using next():")
    iterator = iter(counter)
    try:
        while True:
            number = next(iterator)
            print(number)
    except StopIteration:
        print("Finished counting manually!")

    print("\nIteration using for-loop:")
    # Recreate the iterator (since previous is exhausted)
    for number in CountUpTo(5):
        print(number)
