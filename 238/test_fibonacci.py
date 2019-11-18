from fibonacci import fib
import unittest


class TestFibonnaciNumbers(unittest.TestCase):
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fib(-1)

    def test_first_two_fibonaccis(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_some_fibonaccis(self):
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(6), 8)
