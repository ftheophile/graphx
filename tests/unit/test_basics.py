import unittest

from basics import adder, MyClass


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


class TestNumbers(unittest.TestCase):

    def test_oneNumbers(self):
        mc = MyClass()
        mc.add_number(5)
        self.assertListEqual(mc.get_numbers(), [5])
        del mc

    def test_twoNumbers(self):
        mc = MyClass()
        mc.add_number(15)
        mc.add_number(6)
        self.assertListEqual(mc.get_numbers(), [15, 6])
        del mc


if __name__ == '__main__':
    unittest.main()
