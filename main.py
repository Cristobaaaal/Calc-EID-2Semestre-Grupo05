"""
Video del Grupo 5: "Acumulación a partir de una tasa variable".

Todo está en este archivo. Cada escena es una clase; VideoCompleto las junta.

    manim -pql main.py Escena4_Riemann      # probar una escena
    manim -qh main.py VideoCompleto         # video final 1080p60
"""

from manim import *

# =====================================================================
# 1. EL MODELO MATEMÁTICO
# =====================================================================
A, B = 0, 4          # intervalo de tiempo [0, 4] en segundos
TAMANO = 100         # tamaño del archivo juego.zip en MB


def r(t):
    """Velocidad de descarga en MB/s."""
    return 2 + t


def D(t):
    """MB descargados entre 0 y t: la integral de r, que es 2t + t²/2."""
    return 2 * t + t**2 / 2


def S(n):
    """Suma de Riemann con n rectángulos y extremos izquierdos."""
    dt = (B - A) / n
    return sum(r(A + i * dt) * dt for i in range(n))


# =====================================================================
# 2. COLORES Y PIEZAS QUE SE REPITEN
# =====================================================================
config.background_color = "#0B1426"
Text.set_default(font="Segoe UI")   # en Mac se puede usar "Helvetica Neue"
NARANJA = "#FF9F43"   # velocidad
CIAN = "#35C8F5"      # datos acumulados
VERDE = "#3DDC97"     # resultado exacto
ROSA = "#FF5C8A"      # error de la aproximación


def crear_grafica():
    """Ejes tiempo-velocidad y la recta r(t) = 2 + t."""
    ejes = Axes(
        x_range=[0, 4.6, 1], y_range=[0, 6.8, 1],
        x_length=6, y_length=4.2,
        axis_config={"include_numbers": True, "font_size": 24, "color": GREY_B},
    )
    etiquetas = ejes.get_axis_labels(
        Text("t (s)", font_size=22), Text("r (MB/s)", font_size=22)
    )
    return ejes, etiquetas


def titulo(texto, quien):
    """Título de la escena arriba a la izquierda y quién explica a la derecha."""
    t = Text(texto, font_size=30, weight=BOLD).to_corner(UL)
    q = Text("Explica: " + quien, font_size=20, color=GREY_B).to_corner(UR)
    return VGroup(t, q)


def columna_derecha(*objetos):
    """Apila objetos a la derecha de la pantalla y los achica si no caben."""
    col = VGroup(*objetos).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
    if col.width > 6.2:
        col.scale_to_fit_width(6.2)
    if col.height > 6.2:
        col.scale_to_fit_height(6.2)
    return col.move_to([3.7, -0.35, 0])


# =====================================================================
# 3. ESCENAS
# =====================================================================
class Escena1_Presentacion(Scene):
    def construct(self):
        curso = Text("MAT1134 · Cálculo Intermedio · Grupo 5", font_size=26, color=CIAN)
        tema = Text("Acumulación a partir de una tasa variable", font_size=44, weight=BOLD)
        pregunta = Text(
            "¿Cómo una tasa que cambia con el tiempo\nproduce una cantidad acumulada?",
            font_size=32, t2c={"tasa": NARANJA, "cantidad acumulada": CIAN},
        )
        nombres = Text("Franco Lillo   ·   José Sepúlveda   ·   Cristóbal Dapellus", font_size=26)
        VGroup(curso, tema, pregunta, nombres).arrange(DOWN, buff=0.6)

        self.play(FadeIn(curso), Write(tema), run_time=2.5)
        self.wait(1.5)
        self.play(FadeIn(nombres), run_time=1.5)
        self.wait(5)
        self.play(FadeIn(pregunta), run_time=1.5)
        self.wait(10.5)
        self.play(FadeOut(*self.mobjects))


class Escena2_Descarga(Scene):
    def construct(self):
        self.add(titulo("La situación: descargar juego.zip (100 MB)", "Franco Lillo"))
        ejes, etiquetas = crear_grafica()
        VGroup(ejes, etiquetas).to_edge(RIGHT).shift(DOWN * 0.3)
        recta = ejes.plot(r, x_range=[A, B], color=NARANJA, stroke_width=5)
        formula = MathTex(r"r(t) = 2 + t \qquad 0 \le t \le 4", font_size=44)
        formula.next_to(ejes, UP, buff=0.5)

        self.play(Create(ejes), FadeIn(etiquetas), Write(formula), run_time=2.5)
        self.wait(4)
        self.play(Create(recta), run_time=2)

        # Un solo número controla el tiempo
        t = ValueTracker(0)
        punto = always_redraw(lambda: Dot(ejes.c2p(t.get_value(), r(t.get_value())), color=WHITE))

        # Panel de la izquierda: tiempo y velocidad actuales
        reloj = DecimalNumber(0, num_decimal_places=1, font_size=48)
        reloj.add_updater(lambda m: m.set_value(t.get_value()))
        velocidad = DecimalNumber(2, num_decimal_places=1, font_size=48, color=NARANJA)
        velocidad.add_updater(lambda m: m.set_value(r(t.get_value())))
        panel = VGroup(
            VGroup(Text("Tiempo:", font_size=30), reloj, Text("s", font_size=30)).arrange(RIGHT),
            VGroup(Text("Velocidad:", font_size=30), velocidad, Text("MB/s", font_size=30)).arrange(RIGHT),
            VGroup(Text("Descargado:", font_size=30), Text("? MB", font_size=30, color=CIAN)).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(LEFT, buff=0.8)

        self.play(FadeIn(panel), FadeIn(punto), run_time=1.5)
        self.wait(2)
        self.play(t.animate.set_value(4), run_time=8, rate_func=linear)
        self.wait(2)

        condicion = Text("r es continua y no negativa en [0, 4]", font_size=24, color=GREY_B)
        condicion.next_to(panel, DOWN, buff=0.8)
        self.play(FadeIn(condicion))
        self.wait(3)
        pregunta = Text("¿Cuántos MB se descargaron en 4 segundos?", font_size=32, weight=BOLD).to_edge(DOWN)
        self.play(Write(pregunta))
        self.wait(5)
        self.play(FadeOut(*self.mobjects))


class Escena3_Constante(Scene):
    def construct(self):
        self.add(titulo("Primero, velocidad constante", "Franco Lillo"))
        ejes, etiquetas = crear_grafica()
        VGroup(ejes, etiquetas).to_edge(LEFT).shift(DOWN * 0.3)
        constante = ejes.plot(lambda t: 5, x_range=[A, B], color=NARANJA, stroke_width=5)
        rectangulo = ejes.get_area(constante, x_range=[A, B], color=CIAN, opacity=0.5)

        idea = Text("velocidad × tiempo = cantidad", font_size=28, color=GREY_B)
        producto = MathTex(r"5\ \tfrac{\text{MB}}{\text{s}} \times 4\ \text{s} = 20\ \text{MB}", font_size=42)
        unidades = MathTex(r"\frac{\text{MB}}{\text{s}} \cdot \text{s} = \text{MB}", font_size=40, color=CIAN)
        duda = Text("¿Qué velocidad multiplicamos ahora?", font_size=28, weight=BOLD)
        clave = Text("El área bajo la gráfica\nsigue siendo la cantidad acumulada", font_size=28, color=CIAN)
        columna_derecha(idea, producto, unidades, duda, clave)

        self.play(Create(ejes), FadeIn(etiquetas), run_time=1.5)
        self.play(Create(constante), run_time=1.5)
        self.wait(2)
        self.play(FadeIn(rectangulo), run_time=2)
        dentro = MathTex(r"20\ \text{MB}", font_size=44).move_to(ejes.c2p(2, 2.5))
        self.play(Write(dentro))

        self.play(FadeIn(idea))
        self.play(Write(producto), run_time=2)
        self.wait(3)
        self.play(Write(unidades), run_time=2)
        self.wait(4)

        # La velocidad deja de ser constante: la tapa se inclina
        recta = ejes.plot(r, x_range=[A, B], color=NARANJA, stroke_width=5)
        area = ejes.get_area(recta, x_range=[A, B], color=CIAN, opacity=0.5)
        nuevo = MathTex(r"?\ \text{MB}", font_size=44).move_to(ejes.c2p(2, 1.8))
        self.play(
            Transform(constante, recta), Transform(rectangulo, area), Transform(dentro, nuevo),
            VGroup(idea, producto, unidades).animate.set_opacity(0.3), run_time=3,
        )
        self.wait(2)
        self.play(FadeIn(duda))
        self.wait(3.5)
        self.play(FadeIn(clave))
        self.wait(6)
        self.play(FadeOut(*self.mobjects))


class Escena4_Riemann(Scene):
    def construct(self):
        self.add(titulo("Suma de Riemann con 4 rectángulos", "José Sepúlveda"))
        ejes, etiquetas = crear_grafica()
        VGroup(ejes, etiquetas).to_edge(LEFT).shift(DOWN * 0.3)
        recta = ejes.plot(r, x_range=[A, B], color=NARANJA, stroke_width=5)

        # Columna de la derecha: se arma completa y después se escribe de a poco
        dt = MathTex(r"\Delta t = \frac{b-a}{n} = \frac{4-0}{4} = 1\ \text{s}", font_size=40)
        aporte = MathTex(r"\text{aporte} = r(t_i^*)\cdot\Delta t \quad (\text{MB})", font_size=38)
        filas = VGroup(*[
            MathTex(f"r({i})\\cdot 1 = {r(i)}\\cdot 1 = {r(i)}\\ \\text{{MB}}", font_size=36)
            for i in range(4)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        suma = MathTex(r"S_4 = 2 + 3 + 4 + 5 = 14\ \text{MB}", font_size=42, color=CIAN)
        general = MathTex(r"S_n = \sum_{i=1}^{n} r(t_i^*)\,\Delta t", font_size=40)
        columna_derecha(dt, aporte, filas, suma, general)

        self.play(Create(ejes), FadeIn(etiquetas), Create(recta), run_time=2.5)
        self.play(Write(dt), run_time=2.5)
        self.wait(3)
        self.play(Write(aporte), run_time=2)
        self.wait(4)

        # Manim construye los rectángulos: ancho dx = 1, altura en el extremo izquierdo
        rects = ejes.get_riemann_rectangles(
            recta, x_range=[A, B], dx=1, input_sample_type="left",
            color=CIAN, fill_opacity=0.6, stroke_color=BLACK,
        )
        for i in range(4):
            punto = Dot(ejes.c2p(i, r(i)), color=YELLOW)
            self.play(FadeIn(punto), run_time=0.6)
            self.play(GrowFromEdge(rects[i], DOWN), Write(filas[i]), run_time=1.5)
            self.wait(3)
            self.play(FadeOut(punto), run_time=0.4)

        self.play(Write(suma), run_time=2)
        self.wait(3)
        self.play(Write(general), run_time=2)
        self.wait(4)

        # Lo que no cubren los rectángulos: el área completa en rosado, detrás de ellos
        falta = ejes.get_area(recta, x_range=[A, B], color=ROSA, opacity=0.8)
        aviso = Text("Estimación por debajo: falta lo rosado", font_size=24, color=ROSA)
        aviso.next_to(ejes, DOWN, buff=0.5)
        self.add(falta)
        self.bring_to_front(rects, recta)
        self.play(FadeIn(falta), FadeIn(aviso), run_time=2)
        self.wait(6)
        self.play(FadeOut(*self.mobjects))


class Escena5_Refinamiento(Scene):
    def construct(self):
        self.add(titulo("Más rectángulos, mejor aproximación", "José Sepúlveda"))
        ejes, etiquetas = crear_grafica()
        VGroup(ejes, etiquetas).to_edge(LEFT).shift(DOWN * 0.3)
        recta = ejes.plot(r, x_range=[A, B], color=NARANJA, stroke_width=5)
        falta = ejes.get_area(recta, x_range=[A, B], color=ROSA, opacity=0.8)

        def rectangulos(n):
            return ejes.get_riemann_rectangles(
                recta, x_range=[A, B], dx=(B - A) / n, input_sample_type="left",
                color=CIAN, fill_opacity=0.6, stroke_color=BLACK, stroke_width=max(0.3, 4 / n),
            )

        def datos(n):
            filas = VGroup(
                MathTex(f"n = {n}", font_size=40),
                MathTex(r"\Delta t = " + f"{(B - A) / n:g}" + r"\ \text{s}", font_size=40),
                MathTex(r"S_n = " + f"{S(n):g}" + r"\ \text{MB}", font_size=40, color=CIAN),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            return filas.move_to([1.0, 2.0, 0], aligned_edge=LEFT)

        n = 4
        rects = rectangulos(n)
        tabla = datos(n)
        self.add(falta)
        self.play(FadeIn(ejes), FadeIn(etiquetas), FadeIn(rects), Create(recta), run_time=2)
        self.play(Write(tabla), run_time=1.5)
        self.wait(2.5)

        exacto = MathTex(r"\text{Exacto (trapecio): } \frac{2+6}{2}\cdot 4 = 16\ \text{MB}", font_size=36, color=VERDE)
        exacto.scale_to_fit_width(5.6).move_to([1.0, 0.2, 0], aligned_edge=LEFT)
        self.play(Write(exacto), run_time=2)
        self.wait(5)

        for n in [8, 16, 32, 64]:
            self.play(Transform(rects, rectangulos(n)), Transform(tabla, datos(n)), run_time=2)
            self.bring_to_front(recta)
            self.wait(2.5)

        formula = MathTex(r"S_n = 16 - \frac{8}{n}", font_size=44).move_to([1.0, -1.3, 0], aligned_edge=LEFT)
        self.play(Write(formula), run_time=2)
        self.wait(3.5)
        limite = MathTex(r"n \to \infty,\quad \Delta t \to 0,\quad S_n \to 16\ \text{MB}", font_size=40, color=VERDE)
        limite.scale_to_fit_width(5.6).move_to([1.0, 2.0, 0], aligned_edge=LEFT)
        self.play(Transform(tabla, limite), run_time=2)
        self.wait(3)

        area = ejes.get_area(recta, x_range=[A, B], color=CIAN, opacity=0.6)
        integral = MathTex(
            r"\int_0^4 (2+t)\,dt = \lim_{n\to\infty} \sum_{i=1}^{n} r(t_i^*)\,\Delta t = 16\ \text{MB}",
            font_size=36,
        ).scale_to_fit_width(5.8).move_to([1.0, -1.5, 0], aligned_edge=LEFT)
        self.play(FadeOut(rects), FadeOut(falta), FadeIn(area), FadeOut(formula), run_time=2)
        self.play(Write(integral), run_time=3)
        self.wait(7)
        self.play(FadeOut(*self.mobjects))


class Escena6_Integral(Scene):
    def construct(self):
        self.add(titulo("Calcular la integral", "Cristóbal Dapellus"))
        pasos = VGroup(
            MathTex(r"\int_0^4 (2+t)\,dt", font_size=50),
            MathTex(r"D(t) = 2t + \frac{t^2}{2} \quad\text{porque}\quad D'(t) = 2 + t", font_size=40),
            MathTex(r"= \left[\,2t + \frac{t^2}{2}\,\right]_0^4", font_size=42),
            MathTex(r"= \left(2\cdot 4 + \frac{4^2}{2}\right) - \left(2\cdot 0 + \frac{0^2}{2}\right)", font_size=42),
            MathTex(r"= 8 + 8 - 0", font_size=42),
            MathTex(r"= 16\ \text{MB}", font_size=50, color=VERDE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        pasos.scale_to_fit_height(6.1).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        pausas = [3, 4, 3, 4, 2.5, 4]   # tiempo para hablar después de cada paso
        for paso, pausa in zip(pasos, pausas):
            self.play(Write(paso), run_time=1.8)
            self.wait(pausa)

        caja = SurroundingRectangle(pasos[-1], color=VERDE)
        general = MathTex(r"D(t) = \int_0^t (2+u)\,du = 2t + \frac{t^2}{2}", font_size=40, color=CIAN)
        nota = Text("MB descargados hasta el instante t", font_size=24, color=GREY_B)
        VGroup(general, nota).arrange(DOWN).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.5)
        self.play(Create(caja))
        self.play(Write(general), FadeIn(nota), run_time=2)
        self.wait(5)
        self.play(FadeOut(*self.mobjects))


class Escena7_Sincronizada(Scene):
    def construct(self):
        self.add(titulo("Velocidad, área y descarga a la vez", "Cristóbal Dapellus"))
        ejes, etiquetas = crear_grafica()
        VGroup(ejes, etiquetas).to_edge(RIGHT).shift(DOWN * 0.3)
        recta = ejes.plot(r, x_range=[A, B], color=NARANJA, stroke_width=5)

        # UN SOLO ValueTracker: todo lo demás se calcula a partir de t
        t = ValueTracker(0.001)
        area = always_redraw(lambda: ejes.get_area(recta, x_range=[A, t.get_value()], color=CIAN, opacity=0.6))
        punto = always_redraw(lambda: Dot(ejes.c2p(t.get_value(), r(t.get_value())), color=WHITE))

        # Ventana de descarga
        ventana = RoundedRectangle(width=5.6, height=4.2, corner_radius=0.25, color=GREY_B,
                                   fill_color="#121F3A", fill_opacity=1).to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)
        nombre = Text("juego.zip   (100 MB)", font_size=28, weight=BOLD).move_to(ventana.get_top() + DOWN * 0.6)
        fondo_barra = Rectangle(width=4.6, height=0.3, color=GREY_D, fill_opacity=1).next_to(nombre, DOWN, buff=0.5)
        barra = always_redraw(lambda: Rectangle(
            width=max(0.001, 4.6 * D(t.get_value()) / TAMANO), height=0.3,
            color=CIAN, fill_opacity=1, stroke_width=0,
        ).align_to(fondo_barra, LEFT).align_to(fondo_barra, DOWN))

        def contador(funcion, unidad, color):
            numero = DecimalNumber(0, num_decimal_places=1, font_size=40, color=color)
            numero.add_updater(lambda m: m.set_value(funcion(t.get_value())))
            return VGroup(numero, Text(unidad, font_size=28, color=color)).arrange(RIGHT, buff=0.2)

        lineas = VGroup(
            contador(D, "MB descargados", CIAN),
            contador(lambda x: D(x) / TAMANO * 100, "% del archivo", VERDE),
            contador(r, "MB/s", NARANJA),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(fondo_barra, DOWN, buff=0.4)

        self.play(Create(ejes), FadeIn(etiquetas), Create(recta), FadeIn(ventana), FadeIn(nombre), FadeIn(fondo_barra), run_time=2)
        self.add(area, punto, barra, lineas)
        self.wait(4)
        self.play(t.animate.set_value(2), run_time=6, rate_func=linear)
        self.play(Indicate(lineas[0]), run_time=1.5)
        self.wait(3.5)
        self.play(t.animate.set_value(4), run_time=6, rate_func=linear)
        self.play(Indicate(lineas[0]), Indicate(lineas[1]), run_time=1.5)
        self.wait(5)
        self.play(FadeOut(*self.mobjects))


class Escena8_Cierre(Scene):
    def construct(self):
        self.add(titulo("Respuesta a la pregunta central", "los tres"))
        integral = MathTex(r"\int_0^4 (2+t)\,dt = 16\ \text{MB} \;\to\; 16\,\%\ \text{de juego.zip}", font_size=50)
        caja = SurroundingRectangle(integral, color=VERDE, buff=0.3)
        respuesta = Text(
            "Cada pequeño intervalo aporta r(t)·Δt megabytes.\n"
            "La integral definida es el límite de la suma de esos aportes:\n"
            "la cantidad acumulada.",
            font_size=30, t2c={"r(t)·Δt": NARANJA, "la cantidad acumulada.": CIAN},
        )
        VGroup(VGroup(integral, caja), respuesta).arrange(DOWN, buff=1)
        self.play(Write(integral), Create(caja), run_time=3)
        self.wait(5)
        self.play(FadeIn(respuesta), run_time=2)
        self.wait(14)
        self.play(FadeOut(*self.mobjects))


class Escena9_Creditos(Scene):
    def construct(self):
        creditos = VGroup(
            Text("Créditos y fuentes", font_size=40, weight=BOLD),
            Text("Franco Lillo · José Sepúlveda · Cristóbal Dapellus — Grupo 5, MAT1134", font_size=24, color=CIAN),
            Text("Equipo docente MAT1188 (2026). Introducción a la integral. Apunte base.", font_size=22),
            Text("Stewart, J. (2012). Cálculo de una variable. Trascendentes tempranas, 7.ª ed. Cengage.", font_size=22),
            Text("Thomas, G., Weir, M. y Hass, J. (2010). Cálculo. Una variable, 12.ª ed. Pearson.", font_size=22),
            Text("Strang, G. y Herman, E. (2016). Calculus Volume 1. OpenStax.", font_size=22),
            Text("The Manim Community Developers. Manim Community v0.22. docs.manim.community", font_size=22),
            Text("Uso de inteligencia artificial declarado en el repositorio (IA.md)", font_size=20, color=GREY_B),
        ).arrange(DOWN, buff=0.35)
        self.play(FadeIn(creditos), run_time=2)
        self.wait(13)
        self.play(FadeOut(creditos))


class VideoCompleto(Scene):
    """Todas las escenas seguidas en un solo MP4."""

    def construct(self):
        for escena in [Escena1_Presentacion, Escena2_Descarga, Escena3_Constante,
                       Escena4_Riemann, Escena5_Refinamiento, Escena6_Integral,
                       Escena7_Sincronizada, Escena8_Cierre, Escena9_Creditos]:
            escena.construct(self)
