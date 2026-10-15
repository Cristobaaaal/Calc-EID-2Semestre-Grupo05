"""EID Grupo 5: descarga simulada, sumas de Riemann e integral.

Renderizar: manim -pql descarga_gta.py IntroduccionDescarga
"""

from manim import (
    Axes, BLUE_C, Brace, Create, DashedLine, DecimalNumber, Dot, DOWN,
    FadeIn, FadeOut, GREEN_C, LEFT, MathTex, Rectangle, ReplacementTransform,
    RoundedRectangle, Scene, Text, UP, ValueTracker, VGroup, Write, YELLOW_C,
    always_redraw, linear,
)

from modelo_descarga import DURACION_S, PLAN_MBPS, TAMANO_GB, datos_mb, tasa_mb_s, aportes_izquierdos_mb

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


class AportesDescarga(Scene):
    """Interpreta un rectángulo y suma cinco aportes izquierdos en MB."""

    def construct(self):
        n = 5
        dt = DURACION_S / n
        aportes = aportes_izquierdos_mb(n)
        titulo = Text("De la velocidad a los datos descargados", font_size=34,
                      color=COLOR_TEXTO).to_edge(UP, buff=0.35)
        subtitulo = Text("5 intervalos iguales · velocidad al inicio de cada intervalo",
                         font_size=22, color=COLOR_SECUNDARIO).move_to([0, 2.75, 0])
        ejes = Axes(
            x_range=[0, 4500, 1500], y_range=[0, 60, 20],
            x_length=6.5, y_length=3.2,
            axis_config={"include_tip": False, "color": COLOR_SECUNDARIO},
            x_axis_config={"numbers_to_include": [1500, 3000, 4500]},
            y_axis_config={"numbers_to_include": [20, 40, 60]},
        ).move_to([-3.1, 0.1, 0])
        x_label = Text("Tiempo (s)", font_size=19,
                       color=COLOR_SECUNDARIO).next_to(ejes, DOWN, buff=0.2)
        y_label = Text("MB/s", font_size=19,
                       color=COLOR_SECUNDARIO).next_to(ejes.y_axis, UP, buff=0.1)
        curva = ejes.plot(tasa_mb_s, x_range=[0, DURACION_S], color=GREEN_C)
        rectangulos = VGroup()
        puntos = VGroup()
        # Cada rectángulo usa exactamente el mismo dt que el cálculo numérico.
        for i in range(n):
            x = i * dt
            altura = tasa_mb_s(x)
            rectangulos.add(Rectangle(
                width=ejes.c2p(x + dt, 0)[0] - ejes.c2p(x, 0)[0],
                height=ejes.c2p(0, altura)[1] - ejes.c2p(0, 0)[1],
                fill_color=BLUE_C, fill_opacity=0.45,
                stroke_color=BLUE_C, stroke_width=1.5,
            ).move_to(ejes.c2p(x + dt / 2, altura / 2)))
            puntos.add(Dot(ejes.c2p(x, altura), radius=0.055, color=YELLOW_C))

        formula = MathTex(r"\Delta A_i\approx r(t_i^*)\,\Delta t",
                          font_size=36).move_to([3.7, 1.65, 0])
        unidades = MathTex(r"\frac{\mathrm{MB}}{\mathrm{s}}\cdot\mathrm{s}=\mathrm{MB}",
                           font_size=32, color=GREEN_C).move_to([3.7, 0.7, 0])
        ejemplo = VGroup(
            Text("Primer intervalo", font_size=24, color=YELLOW_C),
            MathTex(r"20\;\mathrm{MB/s}\times\frac{6000}{7}\;\mathrm{s}", font_size=30),
            MathTex(r"\approx 17142.86\;\mathrm{MB}", font_size=30),
            MathTex(r"\approx 17.14\;\mathrm{GB}", font_size=30, color=GREEN_C),
        ).arrange(DOWN, buff=0.25).move_to([3.7, -0.9, 0])
        ancho = Brace(rectangulos[0], DOWN, buff=0.07, color=YELLOW_C)
        ancho_texto = MathTex(r"\Delta t\approx857.14\;\mathrm{s}",
                             font_size=24, color=YELLOW_C).next_to(ancho, DOWN, buff=0.08)
        explicacion = Text("La altura es una tasa; el área del rectángulo representa datos.",
                           font_size=23, color=COLOR_TEXTO).move_to([0, -2.85, 0])
        nota = Text("Modelo hipotético de GTA VI · 1 GB = 1000 MB · valores redondeados",
                    font_size=18, color=COLOR_SECUNDARIO).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(titulo), FadeIn(subtitulo))
        self.play(Create(ejes), FadeIn(x_label), FadeIn(y_label), Create(curva))
        self.play(FadeIn(rectangulos[0]), FadeIn(puntos[0]), Write(formula))
        self.play(FadeIn(ancho), FadeIn(ancho_texto), Write(unidades))
        self.play(FadeIn(ejemplo), FadeIn(explicacion), FadeIn(nota))
        self.wait(6)

        self.play(FadeOut(ejemplo), FadeOut(ancho), FadeOut(ancho_texto),
                  FadeOut(explicacion), FadeOut(formula), FadeOut(unidades))
        sumatoria = MathTex(r"S_5=\sum_{i=1}^{5}r(t_i^*)\,\Delta t",
                            font_size=34).move_to([3.7, 1.65, 0])
        etiqueta_total = Text("Suma aproximada (GB)", font_size=24,
                              color=COLOR_SECUNDARIO).move_to([3.7, 0.75, 0])
        total = DecimalNumber(aportes[0] / 1000, num_decimal_places=2,
                              group_with_commas=False, font_size=48,
                              color=GREEN_C).move_to([3.7, -0.05, 0])
        self.play(Write(sumatoria), FadeIn(etiqueta_total), FadeIn(total))
        for i in range(1, n):
            incremento = Text(f"+ {aportes[i] / 1000:.2f} GB", font_size=28,
                              color=YELLOW_C).move_to([3.7, -0.9, 0])
            self.play(FadeIn(rectangulos[i]), FadeIn(puntos[i]), FadeIn(incremento))
            self.play(total.animate.set_value(sum(aportes[:i + 1]) / 1000))
            self.wait(0.6)
            self.play(FadeOut(incremento), run_time=0.3)
        comparacion = MathTex(r"137.14\;\mathrm{GB}<150\;\mathrm{GB}", font_size=29,
                             color=YELLOW_C).move_to([3.7, -1.15, 0])
        conclusion = VGroup(
            Text("La tasa aumenta: los rectángulos izquierdos quedan bajo la curva.",
                 font_size=22, color=COLOR_TEXTO),
            Text("Subestimamos los datos descargados. ¿Qué pasa con intervalos más pequeños?",
                 font_size=21, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.18).move_to([0, -2.8, 0])
        self.play(FadeIn(comparacion), FadeIn(conclusion))
        self.wait(6)


class IntegralDescarga(Scene):
    """Refina sumas izquierdas y responde la pregunta central mediante el límite."""

    def construct(self):
        titulo = Text("Intervalos más pequeños, una mejor aproximación",
                      font_size=32, color=COLOR_TEXTO).to_edge(UP, buff=0.4)
        regla = MathTex(r"\Delta t=\frac{T}{n},\qquad T=\frac{30000}{7}\;\mathrm{s}",
                        font_size=32).move_to([0, 2.65, 0])
        ejes = Axes(
            x_range=[0, 4500, 1500], y_range=[0, 60, 20],
            x_length=6.5, y_length=3.2,
            axis_config={"include_tip": False, "color": COLOR_SECUNDARIO},
            x_axis_config={"numbers_to_include": [1500, 3000, 4500]},
            y_axis_config={"numbers_to_include": [20, 40, 60]},
        ).move_to([-3.1, 0.05, 0])
        etiqueta_x = Text("Tiempo (s)", font_size=20,
                          color=COLOR_SECUNDARIO).next_to(ejes, DOWN, buff=0.15)
        etiqueta_y = Text("MB/s", font_size=20,
                          color=COLOR_SECUNDARIO).next_to(ejes.y_axis, UP, buff=0.1)
        curva = ejes.plot(tasa_mb_s, x_range=[0, DURACION_S], color=GREEN_C)
        tabla = VGroup(Text("n", font_size=25), Text("Suma (GB)", font_size=25))
        tabla[0].move_to([2.5, 1.75, 0])
        tabla[1].move_to([4.7, 1.75, 0])
        rectangulos = None
        filas = VGroup()
        self.play(FadeIn(titulo), Write(regla))
        self.play(Create(ejes), FadeIn(etiqueta_x), FadeIn(etiqueta_y), Create(curva))
        self.play(FadeIn(tabla))
        for indice, n in enumerate((5, 10, 20, 40, 80)):
            dt = DURACION_S / n
            nuevos = VGroup()
            for i in range(n):
                x = i * dt
                altura = tasa_mb_s(x)
                nuevos.add(Rectangle(
                    width=ejes.c2p(x + dt, 0)[0] - ejes.c2p(x, 0)[0],
                    height=ejes.c2p(0, altura)[1] - ejes.c2p(0, 0)[1],
                    fill_color=BLUE_C, fill_opacity=0.5,
                    stroke_color=BLUE_C, stroke_width=0.7,
                ).move_to(ejes.c2p(x + dt / 2, altura / 2)))
            valor = sum(aportes_izquierdos_mb(n)) / 1000
            fila = VGroup(
                Text(str(n), font_size=27, color=COLOR_TEXTO)
                .move_to([2.5, 1.0 - indice * 0.6, 0]),
                Text(f"{valor:.2f}", font_size=27, color=GREEN_C)
                .move_to([4.7, 1.0 - indice * 0.6, 0]),
            )
            filas.add(fila)
            cambio = FadeIn(nuevos) if rectangulos is None else ReplacementTransform(rectangulos, nuevos)
            self.play(cambio, FadeIn(fila), run_time=1.2)
            # La curva queda sobre los rectángulos para distinguir el error.
            self.bring_to_front(curva)
            rectangulos = nuevos
            self.wait(1.5)
        mensaje = Text("Las sumas se acercan a 150 GB; 80 rectángulos aún son una aproximación.",
                       font_size=22, color=COLOR_TEXTO).move_to([0, -2.65, 0])
        self.play(FadeIn(mensaje))
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in list(self.mobjects)])

        titulo_integral = Text("La integral es el límite de estas sumas",
                               font_size=35, color=COLOR_TEXTO).to_edge(UP, buff=0.5)
        limite = MathTex(
            r"\lim_{n\to\infty}\sum_{i=1}^{n}r(t_i^*)\,\Delta t"
            r"=\int_0^T r(t)\,dt",
            font_size=42,
        ).move_to([0, 1.7, 0])
        explicacion = Text("Al aumentar n, el ancho Δt disminuye y la aproximación mejora.",
                           font_size=24, color=COLOR_SECUNDARIO).move_to([0, 0.65, 0])
        evaluacion = MathTex(
            r"\int_0^T(20+0.007t)\,dt"
            r"=\left[20t+0.0035t^2\right]_0^T",
            font_size=36,
        ).move_to([0, -0.4, 0])
        extremo = MathTex(r"T=\frac{30000}{7}\;\mathrm{s}\approx71\;\mathrm{min}\;26\;\mathrm{s}",
                         font_size=29, color=COLOR_SECUNDARIO).move_to([0, -1.35, 0])
        resultado = MathTex(r"150000\;\mathrm{MB}=150\;\mathrm{GB}",
                           font_size=48, color=GREEN_C).move_to([0, -2.35, 0])
        self.play(FadeIn(titulo_integral), Write(limite))
        self.play(FadeIn(explicacion))
        self.wait(3)
        self.play(Write(evaluacion), FadeIn(extremo))
        self.play(Write(resultado))
        self.wait(4)
        self.play(*[FadeOut(obj) for obj in list(self.mobjects)])

        pregunta = Text("¿Cómo una tasa variable produce una cantidad acumulada?",
                        font_size=29, color=COLOR_TEXTO).to_edge(UP, buff=0.7)
        respuesta = VGroup(
            Text("En cada intervalo: tasa × duración ≈ datos descargados.",
                 font_size=27, color=COLOR_TEXTO),
            Text("Sumamos los aportes de todos los intervalos.",
                 font_size=27, color=COLOR_TEXTO),
            Text("La integral expresa el límite de esas sumas.",
                 font_size=29, color=GREEN_C),
        ).arrange(DOWN, buff=0.5).move_to([0, 0.5, 0])
        unidades = MathTex(r"\underbrace{\mathrm{MB/s}}_{\text{tasa}}"
                           r"\times\underbrace{\mathrm{s}}_{\text{tiempo}}"
                           r"=\underbrace{\mathrm{MB}}_{\text{datos}}",
                           font_size=34).move_to([0, -1.5, 0])
        nota = Text("GTA VI: descarga hipotética de 150 GB, desde 0 GB · no es un dato oficial",
                    font_size=19, color=COLOR_SECUNDARIO).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(pregunta))
        for linea in respuesta:
            self.play(FadeIn(linea))
        self.play(Write(unidades), FadeIn(nota))
        self.wait(6)


class VideoCompleto(Scene):
    """Reúne las cuatro partes, sin audio, con pausas para la narración."""

    def construct(self):
        escenas = (IntroduccionDescarga, TasaVariable, AportesDescarga, IntegralDescarga)
        for indice, escena in enumerate(escenas):
            escena.construct(self)
            if indice < len(escenas) - 1:
                # Congelar los indicadores antes de retirar la escena anterior.
                for objeto in self.mobjects:
                    objeto.clear_updaters()
                self.play(*[FadeOut(obj) for obj in list(self.mobjects)], run_time=0.6)
                self.clear()
