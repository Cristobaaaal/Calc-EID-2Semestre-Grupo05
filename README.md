# Calc-EID-2Semestre-Grupo05

## Información del grupo

- Asignatura/curso: MATE1134: Cálculo Intermedio
- Grupo: 05
- Integrantes:
  - José Sepulveda — GitHub: @jose-sepulveda-tyros
  - Franco Lillo — GitHub: @francou-ops
  - Cristóbal Dapellus — GitHub: @Cristobaaaal

## Tema y pregunta central

- Tema asignado: La integral como acumulación
- Pregunta central: ¿Cómo una tasa que cambia con el tiempo produce una cantidad acumulada?
- Ejemplo principal: La descarga de un archivo llamado juego.zip, de 100 MB, con una velocidad que aumenta con el tiempo la cuál está dada por r(t)= 2+t MB/s , 0 <= t <= 4.
  
## Descripción

Este repositorio contiene el código, las dependencias y los recursos necesarios para reconstruir las escenas de Manim Community utilizadas en el video del proyecto. Las animaciones acompañan la explicación matemática del tema y del ejemplo principal.

## Requisitos

- Python: versión 3.13
- Manim Community: versión v0.22.0
- LaTeX: MiKTeX (Windows) o MacTeX (macOS), necesario para las fórmulas

## Instalación

Windows:
winget install MiKTeX.MiKTeX
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

macOS:
brew install python@3.13
brew install --cask mactex-no-gui
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
   
## Ejecución de las escenas

Probar una escena en baja calidad: manim -pql main.py Escena4_Riemann
Video final en 1920 × 1080 a 60 fps: manim -qh main.py VideoCompleto
El MP4 queda en media/videos/main/1080p60/VideoCompleto.mp4, sin audio. Las voces se graban aparte.

## Escenas incluidas

- Escena1_Presentacion
- Escena2_Descarga
- Escena3_Constante
- Escena4_Riemann
- Escena5_Refinamiento
- Escena6_Integral
- Escena7_Sincronizada
- Escena8_Cierre
- Escena9_Creditos

## Estructura del repositorio

   Calc-EID-2Semestre-Grupo05/
   ├── .gitignore
   ├── README.md
   ├── main.py
   ├── requirements.txt

## Fuentes matemáticas

1.Equipo docente MAT1188 (2026). Introducción a la integral. Apunte base.
2.Stewart, J. (2012). Cálculo de una variable. Trascendentes tempranas, 7.ª ed. Cengage.
3.Thomas, G., Weir, M. y Hass, J. (2010). Cálculo. Una variable, 12.ª ed. Pearson.
4.Strang, G. y Herman, E. (2016). Calculus Volume 1. OpenStax.

## Declaración de uso de inteligencia artificial

Se usó inteligencia artificial para el desarrollo de este trabajo.
Herramienta: Claude (Anthropic), usado a través de la aplicación Claude Code, entre el 13 y el 16 de octubre de 2026.

Para qué se usó: 
-El código de las animaciones fue generado por la IA bajo la estricta supervisión de los estudiantes y contrastada con las fuentes ya mencionadas.
-Orden de las escenas y qué debía mostrar cada una: El grupo lo pidió y ordenó, la IA lo implementó.
-Guion de la narración: Borrador de la IA pero modificado por el grupo.
-README.md: Borradores de la IA pero en gran parte escrito por el grupo.

