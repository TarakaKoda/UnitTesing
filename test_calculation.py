import unittest
import calculation


class test_calculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculation.add(1, 5), 6)
        self.assertEqual(calculation.add(9, 2), 11)
        self.assertEqual(calculation.add(-1, -1), -2)
        self.assertEqual(calculation.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(calculation.sub(1, -1), 2)
        self.assertEqual(calculation.sub(-1, -1), 0)
        self.assertEqual(calculation.sub(2, 3), -1)
        self.assertEqual(calculation.sub(6, 4), 2)

    def test_multiplication(self):
        self.assertEqual(calculation.multiplication(4, 2), 8)
        self.assertEqual(calculation.multiplication(-1, 2), -2)
        self.assertEqual(calculation.multiplication(2, 3), 6)

    def test_division(self):
        self.assertEqual(calculation.division(4, 2), 2)
        self.assertEqual(calculation.division(-1, -1), 1)
        self.assertEqual(calculation.division(5, 2), 2.5)
        self.assertRaises(ValueError, calculation.division, 2, 0)
        # or
        with self.assertRaises(ValueError):
            calculation.division(4, 0)




