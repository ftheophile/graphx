import unittest

from basics import adder


class TestAdder(unittest.TestCase):
    def test_add_positive_ints(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = adder(data)
        self.assertEqual(result, 6, "should be 6")

    def test_add_negative_ints(self):
        """
        Test that it can sum a list of integers
        """
        data = [-1, -2, -3]
        result = adder(data)
        self.assertEqual(result, -6, "should be -6")

    def test_mixed_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [-1, 2, -3]
        result = adder(data)
        self.assertEqual(result, -2, "should be -2")


if __name__ == '__main__':
    unittest.main()
