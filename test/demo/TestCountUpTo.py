import unittest

from src.demo.CountUpTo import CountUpTo


class TestCountUpTo(unittest.TestCase):
    """
    Test cases for the CountUpTo class.
    """

    def test_counting_sequence(self):
        """
        Test that CountUpTo correctly counts from 1 to max_count.
        """
        counter = CountUpTo(5)
        expected = [1, 2, 3, 4, 5]
        result = list(counter)  # Convert iterator to list
        self.assertEqual(result, expected)

    def test_single_value(self):
        """
        Test counting up to 1 (edge case).
        """
        counter = CountUpTo(1)
        expected = [1]
        result = list(counter)
        self.assertEqual(result, expected)

    def test_zero_max_count(self):
        """
        Test counting up to 0 should produce an empty list.
        """
        counter = CountUpTo(0)
        expected = []
        result = list(counter)
        self.assertEqual(result, expected)

    def test_manual_iteration(self):
        """
        Test manual iteration using next().
        """
        counter = CountUpTo(3)
        iterator = iter(counter)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)
        with self.assertRaises(StopIteration):
            next(iterator)  # Should raise after reaching the limit


if __name__ == "__main__":
    unittest.main()
