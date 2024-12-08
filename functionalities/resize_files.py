from PIL import Image
import os

"""
Este módulo proporciona una función para redimensionar en lotes las imágenes de un directorio.

Funciones:
- batch_resize(folder_in, folder_out, width, height): Redimensiona todas las imágenes en un directorio y guarda las versiones redimensionadas en un directorio de salida.

Detalles:
- Las imágenes procesadas deben tener extensiones compatibles (.jpeg, .jpg, .png, .gif, .webp).
- Cada imagen redimensionada se guarda con un prefijo "resized_" en el directorio de salida.
- Utiliza la biblioteca Pillow (PIL) para gestionar las operaciones de imagen.

Dependencias:
- PIL (Pillow): Para abrir, redimensionar y guardar imágenes.
- os: Para gestionar archivos y rutas de directorio.

Parámetros:
- folder_in (str): Ruta al directorio que contiene las imágenes originales.
- folder_out (str): Ruta al directorio donde se guardarán las imágenes redimensionadas.
- width (int): Nuevo ancho de las imágenes redimensionadas, en píxeles.
- height (int): Nueva altura de las imágenes redimensionadas, en píxeles.


"""


def batch_resize(folder_in, folder_out, width, height):
    for filename in os.listdir(folder_in):
        if filename.endswith(('.jpeg', '.jpeg', '.png', '.gif', '.webp')):
            img = Image.open(os.path.join(folder_in, filename))
            img = img.resize((width, height))
            img.save(os.path.join(folder_out, f"resized_{filename}"))
            print(f"{filename} Redimensionado")