import unittest
import main

class TestChequeo(unittest.TestCase):
    def test_registrar_venta(self):
        p_unit = 10
        cant = 5
        total = p_unit * cant # 50
        self.assertEqual(main.registrar_venta(p_unit, cant), total)