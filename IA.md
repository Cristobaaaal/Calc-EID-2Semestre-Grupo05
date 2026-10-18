# Declaración de uso de inteligencia artificial

## Herramienta

**Claude (Anthropic)**, usado a través de la aplicación Claude Code, entre el
13 y el 16 de octubre de 2026.

## Para qué se usó

El código de las animaciones fue **generado por la IA**, no escrito por los
integrantes del grupo.

| Parte del proyecto                                                            | ¿Quién lo hizo?                                     |
| ----------------------------------------------------------------------------- | --------------------------------------------------- |
| Tema y pregunta central                                                       | Asignados por el curso                              |
| Ejemplo (descarga de `juego.zip`, `r(t) = 2 + t`, intervalo `[0, 4]`, 100 MB) | El grupo lo propuso; la IA lo desarrolló            |
| Orden de las escenas y qué debía mostrar cada una                             | El grupo lo pidió; la IA lo implementó              |
| Código de `main.py`                                                           | **IA**                                              |
| Cálculos (sumas de Riemann, integral, fórmula `Sₙ = 16 − 8/n`)                | **IA**; el grupo los revisó                         |
| Guion de la narración                                                         | Borrador de la **IA**; el grupo lo adaptó al grabar |
| `README.md`, `referencias.md`                                                 | Borradores de la **IA**                             |
| Grabación de las voces                                                        | El grupo                                            |
| Edición y montaje del video en DaVinci Resolve                                | El grupo                                            |

La IA no generó audio, voces, imágenes ni video: el video sale de ejecutar
`main.py` con Manim Community y las voces son de los integrantes.

## Cómo lo verificamos

- Ejecutamos `main.py` y revisamos que el video mostrara lo que pedimos.
- Rehicimos a mano los cálculos principales y coinciden con el video:
  - `S₄ = 2 + 3 + 4 + 5 = 14 MB`
  - `S₈ = 15 MB`
  - `∫₀⁴ (2 + t) dt = [2t + t²/2]₀⁴ = 8 + 8 = 16 MB`, que es el 16 % de 100 MB
  - Área del trapecio: `(2 + 6)/2 · 4 = 16 MB`
- Contrastamos las definiciones (partición, punto muestra, suma de Riemann,
  integral definida, Teorema Fundamental) con el apunte base del curso.
- Estudiamos el código parte por parte para poder explicarlo
  en la defensa.

## Limitaciones

- No escribimos el código desde cero; nuestro aporte en esa parte fue definir
  qué debía mostrar, revisarlo y entenderlo.
- La lista de fuentes de `referencias.md` la propuso la IA; el grupo la
  revisó y consultó esas fuentes.
