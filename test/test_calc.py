# unitest - part of the standard library. 
# Test cases by subclassing unittest.Testcase.
# cn have multiple tests methods per test case. 
# assertion methods - assertEqual asserTrue.

import unittest 
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_calculator_class_exists(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))

    def test_add_method_accepts_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0,0), 0)

    def test_add_method_with_non_numeric_input(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom Error: Inputs must be numeric"):
            calc.add("a", 5)
    
    def test_add_method_returns_numeric(self):
        calc = Calculator()
        self.assertIsInstance(calc.add(1, 2), (int, float))

    def test_add_method_performs_correct_calculation(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(100, 200), 300)

    @unittest.skip("skipping...")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "skippped...")
    def test_if_skip(self):
        pass



if __name__=='__main__':
    unittest.main()

# run with python3 -m unittest test_calc.py 
