# Python Unit Testing with `unittest` Cheat Sheet

# Importing unittest
import unittest

# Basic Test Structure
class TestExample(unittest.TestCase):
    def setUp(self):
        # Code to run before each test

    def tearDown(self):
        # Code to run after each test

    def test_something(self):
        # Test case for 'something'
        self.assertEqual('foo', 'foo')

    def test_another_thing(self):
        # Another test case
        self.assertTrue(some_condition)

# Assertions
self.assertEqual(a, b)            # a == b
self.assertNotEqual(a, b)         # a != b
self.assertTrue(x)                # bool(x) is True
self.assertFalse(x)               # bool(x) is False
self.assertIs(a, b)               # a is b
self.assertIsNot(a, b)            # a is not b
self.assertIsNone(x)              # x is None
self.assertIsNotNone(x)           # x is not None
self.assertIn(a, b)                # a in b
self.assertNotIn(a, b)            # a not in b
self.assertIsInstance(a, b)       # isinstance(a, b)
self.assertNotIsInstance(a, b)    # not isinstance(a, b)

# Running Tests
if __name__ == '__main__':
    unittest.main()

# Test Suites
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

# Skipping Tests
@unittest.skip("reason for skipping")
def test_function(self):
    # body of skipped test

# Expected Failures
@unittest.expectedFailure
def test_function(self):
    # body of expected failure test

# Testing Exceptions
with self.assertRaises(SomeException):
    # code that should raise SomeException

# Testing Warnings
with self.assertWarns(SomeWarning):
    # code that should raise SomeWarning

# Test Discovery
# Run 'python -m unittest discover' in your project root directory
# By default, it discovers tests in any file named 'test*.py'

# Note: This cheat sheet is an overview of the `unittest` framework in Python and does not cover all aspects.
