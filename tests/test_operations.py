import unittest
import sys
import os

# Agregar src al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator.operations import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
