# EID de Cálculo · Grupo 5

Animación con Manim sobre acumulación a partir de una tasa variable, usando una descarga simulada de GTA VI.

## Primer bloque: introducción

La escena presenta una transferencia supuesta de **150 GB**, un plan de **600 Mbps** y la diferencia entre megabits y megabytes. 600 Mbps equivalen a un máximo teórico de **75 MB/s**; las velocidades del modelo (20 a 50 MB/s) son simuladas y no garantizadas por el plan.

Los **150 GB son un tamaño hipotético para el ejercicio, no un dato oficial** ni una descarga real medida. La gráfica, los rectángulos y la integral se implementarán en los siguientes bloques.

## Instalación en macOS

Requisitos: Python 3.12 o posterior, `uv`, Homebrew y MacTeX (LaTeX y dvisvgm).

Desde la carpeta del repositorio:

```sh
brew install cairo pkg-config
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
```

## Generar el video

```sh
source .venv/bin/activate
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
manim -pql descarga_gta.py IntroduccionDescarga
```

`-p` abre el resultado y `-ql` genera una vista previa a 480p. Para 1080p, reemplaza `-pql` por `-pqh`.

El video de prueba se guarda en `media/videos/descarga_gta/480p15/IntroduccionDescarga.mp4`. La carpeta `media/` y el entorno `.venv/` no se suben a Git.

## Fuentes y diseño

- [AT&T: velocidades y limitaciones de descarga](https://www.att.com/blog/download-speed-vs-upload-speed/).
- [Instalación oficial de Manim](https://docs.manim.community/en/stable/installation/uv.html).
- [Diseño matemático y visual](docs/diseno-manim.md).
- [Plan por bloques](docs/plan-implementacion.md).
