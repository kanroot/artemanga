from django.test import TestCase

class UtilsTestCase(TestCase):
    def test_pedir_color_debe_dar_diferentes_colores(self):
        from analitica.chartjs.utils import obtener_nuevo_color_solido
        color1 = next(obtener_nuevo_color_solido)
        color2 = next(obtener_nuevo_color_solido)
        self.assertNotEqual(color1, color2)

    def test_pedir_mas_colores_que_disponibles_no_levanta_excepcion(self):
        from analitica.chartjs.utils import obtener_nuevo_color_solido
        for i in range(0, 100):
            next(obtener_nuevo_color_solido)
            