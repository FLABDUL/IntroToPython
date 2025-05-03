class GeneratorDemo:
    # A simple generator to generate squares of numbers
    def square_numbers(self, n):
        for i in range(n):
            yield i ** 2

    # A generator to generate an infinite sequence of Fibonacci numbers
    def fibonacci(self):
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # A generator to generate a range of numbers that satisfies a condition
    def filter_even_numbers(self, n):
        for i in range(n):
            if i % 2 == 0:
                yield i

    def run(self):
        print("Squares of numbers:")
        squares = self.square_numbers(5)
        for square in squares:
            print(square)

        print("\nFibonacci numbers (first 10):")
        fib = self.fibonacci()
        for _ in range(10):
            print(next(fib))

        print("\nEven numbers less than 10:")
        evens = self.filter_even_numbers(10)
        for even in evens:
            print(even)

if __name__ == "__main__":
    demo = GeneratorDemo()
    demo.run()
