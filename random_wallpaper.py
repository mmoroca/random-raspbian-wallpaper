#!/usr/bin/env python3
"""
random_wallpaper.py
Selecciona aleatoriamente un fondo de pantalla del directorio de wallpapers
de Raspbian y lo aplica usando pcmanfm.

Uso:
    python3 random_wallpaper.py
    python3 random_wallpaper.py --dir /ruta/personalizada
"""

import os
import random
import subprocess
import argparse
import sys
import logging

# Directorio por defecto de wallpapers en Raspbian
DEFAULT_WALLPAPER_DIR = "/usr/share/rpd-wallpaper"

# Extensiones de imagen soportadas
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".svg", ".webp")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


def get_wallpapers(directory: str) -> list:
    """Devuelve una lista de rutas absolutas de imágenes en el directorio."""
    if not os.path.isdir(directory):
        logger.error(f"El directorio '{directory}' no existe o no es accesible.")
        sys.exit(1)

    wallpapers = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.lower().endswith(IMAGE_EXTENSIONS)
    ]

    if not wallpapers:
        logger.error(f"No se encontraron imágenes en '{directory}'.")
        sys.exit(1)

    return wallpapers


def set_wallpaper(image_path: str) -> None:
    """Aplica el wallpaper usando pcmanfm (gestor de escritorio de Raspbian)."""
    try:
        # pcmanfm necesita la variable DISPLAY para funcionar
        env = os.environ.copy()
        if "DISPLAY" not in env:
            env["DISPLAY"] = ":0"

        subprocess.run(
            ["pcmanfm", "--set-wallpaper", image_path, "--wallpaper-mode", "crop"],
            env=env,
            check=True,
            capture_output=True,
            text=True
        )
        logger.info(f"Wallpaper aplicado: {image_path}")

    except FileNotFoundError:
        logger.error("'pcmanfm' no está instalado. Instálalo con: sudo apt install pcmanfm")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error al aplicar el wallpaper: {e.stderr}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Establece un wallpaper aleatorio en Raspbian al inicio de sesión."
    )
    parser.add_argument(
        "--dir", "-d",
        default=DEFAULT_WALLPAPER_DIR,
        help=f"Directorio de wallpapers (por defecto: {DEFAULT_WALLPAPER_DIR})"
    )
    args = parser.parse_args()

    wallpapers = get_wallpapers(args.dir)
    chosen = random.choice(wallpapers)

    logger.info(f"Wallpapers encontrados: {len(wallpapers)}")
    logger.info(f"Seleccionado: {os.path.basename(chosen)}")

    set_wallpaper(chosen)


if __name__ == "__main__":
    main()
