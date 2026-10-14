"""EID Grupo 5: introducción a una descarga simulada con tasa variable.

Renderizar: manim -pql descarga_gta.py IntroduccionDescarga
"""

from manim import (
    Axes, BLUE_C, Create, DashedLine, DecimalNumber, Dot, DOWN,
    FadeIn, FadeOut, GREEN_C, LEFT, MathTex, Rectangle,
    RoundedRectangle, Scene, Text, UP, ValueTracker, VGroup, Write,
    always_redraw, linear,
)

from modelo_descarga import DURACION_S, PLAN_MBPS, TAMANO_GB, datos_mb, tasa_mb_s

COLOR_TEXTO = "#F1F5F9"
COLOR_SECUNDARIO = "#B8C4D6"


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


class TasaVariable(Scene):
    """Una misma variable de tiempo controla la gráfica y toda la descarga."""

    def construct(self):
        titulo = Text("Una velocidad variable, una descarga que se acumula",
                      font_size=30, color=COLOR_TEXTO).to_edge(UP, buff=0.35)
        formula = MathTex(r"r(t)=20+0.007t", font_size=34,
                          color=GREEN_C).move_to([-2.8, 2.65, 0])
        unidades = Text("t en segundos · r(t) en MB/s", font_size=20,
                        color=COLOR_SECUNDARIO).next_to(formula, DOWN, buff=0.18)
        ejes = Axes(
            x_range=[0, 4500, 1500], y_range=[0, 80, 20],
            x_length=7, y_length=3.5,
            axis_config={"include_tip": False, "color": COLOR_SECUNDARIO},
            x_axis_config={"numbers_to_include": [0, 1500, 3000, 4500]},
            y_axis_config={"numbers_to_include": [20, 40, 60, 80]},
        ).move_to([-2.8, -0.25, 0])
        etiqueta_x = Text("Tiempo (s)", font_size=20,
                          color=COLOR_SECUNDARIO).next_to(ejes, DOWN, buff=0.15)
        etiqueta_y = Text("MB/s", font_size=20, color=COLOR_SECUNDARIO)
        etiqueta_y.next_to(ejes.y_axis, UP, buff=0.1)
        limite = DashedLine(ejes.c2p(0, PLAN_MBPS / 8),
                           ejes.c2p(4500, PLAN_MBPS / 8),
                           color=COLOR_SECUNDARIO, stroke_width=1.5)
        limite_texto = Text("600 Mbps: máximo teórico de 75 MB/s", font_size=16,
                            color=COLOR_SECUNDARIO).next_to(limite, UP, buff=0.08)
        curva = ejes.plot(tasa_mb_s, x_range=[0, DURACION_S], color=GREEN_C)
        tiempo = ValueTracker(0)
        punto = always_redraw(lambda: Dot(
            ejes.c2p(tiempo.get_value(), tasa_mb_s(tiempo.get_value())),
            color=BLUE_C, radius=0.075,
        ))
        guia = always_redraw(lambda: DashedLine(
            ejes.c2p(tiempo.get_value(), 0),
            ejes.c2p(tiempo.get_value(), tasa_mb_s(tiempo.get_value())),
            color=BLUE_C, stroke_width=2,
        ))

        panel = RoundedRectangle(width=4.3, height=4.8, corner_radius=0.2,
                                 color=BLUE_C).move_to([4.1, 0, 0])
        juego = Text("GTA VI · 150 GB", font_size=27,
                     color=COLOR_TEXTO).move_to([4.1, 1.9, 0])
        numeros = VGroup()
        etiquetas = VGroup()
        # Los números cambian sobre un anclaje fijo para no desplazar las unidades.
        metricas = [
            ("Tiempo transcurrido (min)", 1.12, lambda: tiempo.get_value() / 60, 1),
            ("Velocidad actual (MB/s)", 0.12, lambda: tasa_mb_s(tiempo.get_value()), 1),
            ("Datos descargados (GB)", -0.88, lambda: datos_mb(tiempo.get_value()) / 1000, 2),
        ]
        for nombre, y, valor, decimales in metricas:
            etiquetas.add(Text(nombre, font_size=20, color=COLOR_SECUNDARIO)
                          .move_to([4.1, y, 0]))
            numero = DecimalNumber(valor(), num_decimal_places=decimales,
                                   group_with_commas=False, font_size=32,
                                   color=GREEN_C).move_to([4.1, y - 0.4, 0])
            numero.add_updater(lambda m, valor=valor, y=y:
                               m.set_value(valor()).move_to([4.1, y - 0.4, 0]))
            numeros.add(numero)

        barra = Rectangle(width=3.5, height=0.18, color=COLOR_SECUNDARIO,
                          stroke_width=1).move_to([4.1, -1.8, 0])
        relleno = always_redraw(lambda: Rectangle(
            width=max(0.0001, 3.5 * datos_mb(tiempo.get_value()) / (TAMANO_GB * 1000)),
            height=0.18, fill_color=GREEN_C,
            fill_opacity=1 if tiempo.get_value() > 0 else 0, stroke_width=0,
        ).move_to(barra).align_to(barra, LEFT))
        porcentaje = DecimalNumber(0, num_decimal_places=1, unit=r"\%",
                                   font_size=22, color=COLOR_TEXTO).move_to([4.1, -2.15, 0])
        porcentaje.add_updater(lambda m: m.set_value(
            100 * datos_mb(tiempo.get_value()) / (TAMANO_GB * 1000)
        ).move_to([4.1, -2.15, 0]))
        aviso = Text("Simulación acelerada · 150 GB hipotéticos, no oficiales",
                     font_size=20, color=COLOR_SECUNDARIO).to_edge(DOWN, buff=0.3)
        cierre = Text("Mayor velocidad → más datos descargados en cada segundo",
                      font_size=25, color=COLOR_TEXTO).move_to([0, -2.95, 0])

        self.play(FadeIn(titulo), Write(formula), FadeIn(unidades))
        self.play(Create(ejes), FadeIn(etiqueta_x), FadeIn(etiqueta_y))
        self.play(Create(limite), FadeIn(limite_texto), Create(curva))
        self.play(FadeIn(panel), FadeIn(juego), FadeIn(etiquetas),
                  FadeIn(numeros), FadeIn(barra), FadeIn(aviso))
        self.add(relleno, porcentaje, guia, punto)
        self.wait(2)
        self.play(tiempo.animate.set_value(DURACION_S), run_time=18, rate_func=linear)
        self.play(FadeIn(cierre))
        self.wait(4)
