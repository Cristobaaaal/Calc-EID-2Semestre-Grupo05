"""Comprobaciones de unidades y valores del modelo, independientes del render."""
import unittest
from modelo_descarga import DURACION_S, TAMANO_GB, datos_mb, tasa_mb_s


class ModeloDescargaTests(unittest.TestCase):
    def test_inicio_sin_datos_y_tasa_de_20_megabytes(self):
        self.assertEqual(datos_mb(0), 0)
        self.assertEqual(tasa_mb_s(0), 20)

    def test_mil_segundos_acumulan_23500_megabytes(self):
        self.assertAlmostEqual(tasa_mb_s(1000), 27)
        self.assertAlmostEqual(datos_mb(1000), 23500)

    def test_final_de_150_gb_con_tasa_de_50_megabytes(self):
        self.assertAlmostEqual(DURACION_S, 150000 / 35)
        self.assertAlmostEqual(datos_mb(DURACION_S) / 1000, TAMANO_GB)
        self.assertAlmostEqual(tasa_mb_s(DURACION_S), 50)
        self.assertLess(tasa_mb_s(DURACION_S), 600 / 8)


if __name__ == '__main__':
    unittest.main()
