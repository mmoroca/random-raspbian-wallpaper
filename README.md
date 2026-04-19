# Random Raspbian Wallpaper / Fondo Aleatorio para Raspbian

![random raspbian wallpaper](https://raw.githubusercontent.com/mmoroca/random-raspbian-wallpaper/refs/heads/main/screenshot.png)

---

## 🇪🇸 Español

Cambia el fondo de pantalla automáticamente al inicio de sesión eligiendo una imagen al azar del directorio de wallpapers de Raspbian.

### Requisitos

- Raspberry Pi con Raspbian (escritorio)
- Python 3
- `pcmanfm` (preinstalado en Raspbian)

### Uso

```bash
# Directorio por defecto (/usr/share/rpd-wallpaper)
python3 random_wallpaper.py

# Directorio personalizado
python3 random_wallpaper.py --dir /ruta/a/tus/imagenes
```

### Instalación automática al inicio de sesión

Crea el archivo `~/.config/autostart/random-wallpaper.desktop` con este contenido:

```ini
[Desktop Entry]
Type=Application
Name=Random Wallpaper
Exec=python3 /home/pi/random_wallpaper.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
```

### Modos de visualización disponibles

| Modo | Descripción |
|------|-------------|
| `stretch` | Rellena toda la pantalla (puede distorsionar) |
| `fit` | Ajusta respetando la proporción (puede dejar bandas) |
| `center` | Centra sin escalar |
| `tile` | Repite en mosaico |
| `crop` | Recorta para rellenar sin distorsionar |

Para cambiar el modo, edita la línea correspondiente en `random_wallpaper.py`:
```python
["pcmanfm", "--set-wallpaper", image_path, "--wallpaper-mode", "stretch"]
```

---

## 🇬🇧 English

Automatically changes the desktop wallpaper at login by randomly picking an image from Raspbian's wallpaper directory.

### Requirements

- Raspberry Pi running Raspbian (desktop)
- Python 3
- `pcmanfm` (pre-installed on Raspbian)

### Usage

```bash
# Default directory (/usr/share/rpd-wallpaper)
python3 random_wallpaper.py

# Custom directory
python3 random_wallpaper.py --dir /path/to/your/images
```

### Auto-start at login

Create the file `~/.config/autostart/random-wallpaper.desktop` with the following content:

```ini
[Desktop Entry]
Type=Application
Name=Random Wallpaper
Exec=python3 /home/pi/random_wallpaper.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
```

### Available display modes

| Mode | Description |
|------|-------------|
| `stretch` | Fills the entire screen (may distort) |
| `fit` | Fits while preserving aspect ratio (may leave bars) |
| `center` | Centers without scaling |
| `tile` | Repeats as a mosaic |
| `crop` | Crops to fill without distortion |

To change the mode, edit the relevant line in `random_wallpaper.py`:
```python
["pcmanfm", "--set-wallpaper", image_path, "--wallpaper-mode", "stretch"]
```
