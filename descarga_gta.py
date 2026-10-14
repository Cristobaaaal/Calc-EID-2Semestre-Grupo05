"""EID Grupo 5: introducción a una descarga simulada con tasa variable.

Renderizar: manim -pql descarga_gta.py IntroduccionDescarga
"""

from manim import (
    BLUE_C, DOWN, FadeIn, FadeOut, GREEN_C, MathTex,
    RoundedRectangle, Scene, Text, UP, VGroup, Write,
)

COLOR_TEXTO = "#F1F5F9"
COLOR_SECUNDARIO = "#B8C4D6"
PLAN_MBPS = 600
TAMANO_GB = 150  # Tamaño hipotético para el ejercicio; no es un dato oficial.


class IntroduccionDescarga(Scene):
    """Presenta el contexto y las unidades; las gráficas vienen después."""

    def construct(self):
        # Primera pantalla: plantear la situación sin confundir disco y descarga.
        etiqueta = Text("CÁLCULO INTERMEDIO · GRUPO 5", font_size=22,
                        color=BLUE_C).to_edge(UP, buff=0.6)
        titulo = Text("Descargando GTA VI", font_size=40,
                      color=COLOR_TEXTO).shift(UP * 1.5)
        tamano = Text(f"{TAMANO_GB} GB", font_size=72, color=GREEN_C)
        contexto = Text("Tamaño supuesto para nuestra simulación", font_size=26,
                        color=COLOR_TEXTO).next_to(tamano, DOWN, buff=0.3)
        nota = VGroup(
            Text("Tamaño hipotético para el ejercicio; no es un dato oficial.",
                 font_size=20, color=COLOR_SECUNDARIO),
            Text("No representa una descarga real medida de GTA VI.",
                 font_size=20, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(etiqueta), Write(titulo))
        self.play(FadeIn(tamano), FadeIn(contexto), FadeIn(nota))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, tamano, contexto, nota)))

        # Segunda pantalla: un plan en megabits no indica megabytes por segundo.
        plan = Text(f"Tienes contratado un plan de {PLAN_MBPS} Mbps",
                    font_size=34, color=COLOR_TEXTO).shift(UP * 1.8)
        conversion = MathTex(
            r"600\;\mathrm{Mb/s}\div 8 = 75\;\mathrm{MB/s}",
            font_size=48, color=GREEN_C,
        ).shift(UP * 0.6)
        teorico = Text("Máximo teórico: 75 megabytes por segundo",
                       font_size=26, color=COLOR_TEXTO).shift(DOWN * 0.35)
        unidades = Text("b = bit     ·     B = byte     ·     1 byte = 8 bits",
                        font_size=24, color=COLOR_SECUNDARIO).shift(DOWN * 1.15)
        factores = Text("La velocidad efectiva depende de la red y del servidor.",
                        font_size=23, color=COLOR_SECUNDARIO).shift(DOWN * 2.1)
        self.play(FadeIn(plan), Write(conversion))
        self.play(FadeIn(teorico), FadeIn(unidades), FadeIn(factores))
        self.wait(5)
        self.play(FadeOut(VGroup(plan, conversion, teorico, unidades, factores)))

        # Tercera pantalla: anunciar la tasa variable, sin adelantar el cálculo.
        cabecera = Text("La velocidad de descarga puede cambiar",
                        font_size=36, color=COLOR_TEXTO).shift(UP * 1.8)
        marco = RoundedRectangle(width=10.8, height=1.35, corner_radius=0.2,
                                 color=BLUE_C).shift(UP * 0.35)
        velocidad = Text("En nuestro modelo: de 20 a 50 MB/s",
                         font_size=34, color=GREEN_C).move_to(marco)
        aclaracion = Text("Velocidades simuladas; no son una garantía del plan.",
                          font_size=22, color=COLOR_SECUNDARIO).shift(DOWN * 0.8)
        pregunta = VGroup(
            Text("Si la velocidad cambia,", font_size=32, color=COLOR_TEXTO),
            Text("¿cómo calculamos los datos acumulados?", font_size=32,
                 color=COLOR_TEXTO),
        ).arrange(DOWN, buff=0.2).shift(DOWN * 2)
        self.play(FadeIn(cabecera), FadeIn(marco), Write(velocidad))
        self.play(FadeIn(aclaracion), Write(pregunta))
        self.wait(5)
