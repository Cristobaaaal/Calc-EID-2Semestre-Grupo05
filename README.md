# Acumulación a partir de una tasa variable

EID – Introducción a la integral con Manim Community
**MAT1188 – Cálculo Intermedio · Ingeniería Civil Informática · Grupo 5 · 2026**

**Pregunta central:** ¿Cómo una tasa que cambia con el tiempo produce una cantidad acumulada?

**Ejemplo:** se descarga `juego.zip` (100 MB) con velocidad `r(t) = 2 + t` MB/s
durante `0 ≤ t ≤ 4` s. Lo descargado es `∫₀⁴ (2 + t) dt = 16 MB`, el 16 % del archivo.

## Integrantes

| Integrante | Rol principal | GitHub |
|---|---|---|
| Franco Lillo | Matemática y explicación | `@completar` |
| José Sepúlveda | Visualización y código | `@completar` |
| Cristóbal Dapellus | Revisión e integración del video | `@completar` |

## Versiones y dependencias

| Componente | Versión |
|---|---|
| Python | 3.13 |
| Manim Community | 0.22.0 |
| LaTeX | MiKTeX (Windows) o MacTeX (macOS), necesario para las fórmulas |

Dependencias de Python en [requirements.txt](requirements.txt).

## Archivos

| Archivo | Contenido |
|---|---|
| [main.py](main.py) | Todo el código del video: modelo, gráficas y escenas |
| [referencias.md](referencias.md) | Fuentes consultadas |
| [IA.md](IA.md) | Declaración de uso de inteligencia artificial |

### Organización de `main.py`

1. **Modelo matemático:** `r(t)` (velocidad), `D(t)` (MB descargados) y `S(n)`
   (suma de Riemann con extremos izquierdos). Todos los números del video salen de aquí.
2. **Piezas reutilizables:** colores, `crear_grafica()`, `titulo()` y `columna_derecha()`.
3. **Escenas:** una clase por escena y `VideoCompleto`, que las ejecuta seguidas.

## Escenas

| Clase | Contenido | Duración |
|---|---|---|
| `Escena1_Presentacion` | Integrantes, tema y pregunta central | 23 s |
| `Escena2_Descarga` | El modelo `r(t) = 2 + t` y la pregunta | 34 s |
| `Escena3_Constante` | 5 MB/s × 4 s = 20 MB; la recta se inclina | 38 s |
| `Escena4_Riemann` | n = 4, extremos izquierdos, S₄ = 14 MB | 56 s |
| `Escena5_Refinamiento` | n = 4, 8, 16, 32, 64; límite e integral | 55 s |
| `Escena6_Integral` | Cálculo paso a paso: 16 MB | 40 s |
| `Escena7_Sincronizada` | Área, barra y contadores movidos por un solo `ValueTracker` | 31 s |
| `Escena8_Cierre` | Respuesta a la pregunta central | 25 s |
| `Escena9_Creditos` | Fuentes y créditos | 16 s |
| `VideoCompleto` | Todas seguidas | 5 min 17 s |

## Instalación

**Windows**

```bash
winget install MiKTeX.MiKTeX
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**macOS**

```bash
brew install python@3.13
brew install --cask mactex-no-gui
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En macOS conviene cambiar `"Segoe UI"` por `"Helvetica Neue"` en la línea
`Text.set_default(...)` de `main.py`.

## Ejecución

Probar una escena en baja calidad:

```bash
manim -pql main.py Escena4_Riemann
```

Video final en 1920 × 1080 a 60 fps:

```bash
manim -qh main.py VideoCompleto
```

El MP4 queda en `media/videos/main/1080p60/VideoCompleto.mp4`, sin
audio. Las voces se graban aparte.
