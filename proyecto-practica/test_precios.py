import unittest

from precios import precio_con_iva, total


class TestPrecios(unittest.TestCase):
    def test_iva_basico(self):
        self.assertAlmostEqual(precio_con_iva(100), 121)

    def test_total(self):
        self.assertAlmostEqual(total([100, 100], iva=0.1), 220)

    # Estos dos fallan hasta que resuelvas el TODO de precios.py (esa es tu primera tarea).
    def test_redondeo(self):
        self.assertEqual(precio_con_iva(19.99), 24.19)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            precio_con_iva(-1)


if __name__ == "__main__":
    unittest.main()
