import unittest
from calculator import add, subtract, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(6,1),7)
    def test_subtract(self):
        self.assertEqual(subtract(9,4),5)
    def test_multiply(self):
        self.assertEqual(multiply(1,5),5)

if __name__=='__main__':
    unittest.main()