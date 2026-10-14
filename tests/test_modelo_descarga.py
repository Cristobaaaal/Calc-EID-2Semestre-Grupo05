"""Comprobaciones de unidades y valores del modelo, independientes del render."""
import unittest
from modelo_descarga import DURACION_S, TAMANO_GB, datos_mb, tasa_mb_s, aportes_izquierdos_mb


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


class AportesTests(unittest.TestCase):
    def test_cinco_aportes_corresponden_a_velocidades_20_26_32_38_44(self):
        aportes = aportes_izquierdos_mb(5)
        self.assertEqual(len(aportes), 5)
        for aporte, velocidad in zip(aportes, [20, 26, 32, 38, 44]):
            self.assertAlmostEqual(aporte, velocidad * (6000 / 7))

    def test_sumas_se_acercan_al_total_desde_abajo(self):
        esperadas = [(5, 960 / 7), (10, 1005 / 7), (20, 1027.5 / 7)]
        anterior = 0
        for n, gb in esperadas:
            total = sum(aportes_izquierdos_mb(n)) / 1000
            self.assertAlmostEqual(total, gb)
            self.assertGreater(total, anterior)
            self.assertLess(total, 150)
            anterior = total

    def test_rechaza_particiones_sin_un_numero_entero_positivo(self):
        for n in (0, -1, 2.5, True):
            with self.assertRaises(ValueError):
                aportes_izquierdos_mb(n)


if __name__ == '__main__':
    unittest.main()
