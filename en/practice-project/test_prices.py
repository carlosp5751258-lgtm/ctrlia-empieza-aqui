import unittest

from prices import price_with_vat, total


class TestPrices(unittest.TestCase):
    def test_basic_vat(self):
        self.assertAlmostEqual(price_with_vat(100), 121)

    def test_total(self):
        self.assertAlmostEqual(total([100, 100], vat=0.1), 220)

    # These two fail until you resolve the TODO in prices.py (that's your first task).
    def test_rounding(self):
        self.assertEqual(price_with_vat(19.99), 24.19)

    def test_negative(self):
        with self.assertRaises(ValueError):
            price_with_vat(-1)


if __name__ == "__main__":
    unittest.main()
