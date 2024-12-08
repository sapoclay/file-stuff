import os
import platform
import subprocess
import io
from rembg import remove
from PIL import Image

# Función para eliminar el fondo de una imagen
def eliminar_fondo(input_image_path, output_image_path):
    try:
        print(f"Intentando eliminar fondo de la imagen: {input_image_path}")
        with open(input_image_path, "rb") as input_file:
            input_data = input_file.read()

        output_data = remove(input_data)

        img = Image.open(io.BytesIO(output_data)).convert("RGBA")
        img.save(output_image_path, format="PNG")
        print(f"Imagen guardada en: {output_image_path}")
    except Exception as e:
        print(f"Error al eliminar el fondo: {e}")

# Función para eliminar el fondo de imágenes en una carpeta
def eliminar_fondo_carpeta(carpeta_origen, carpeta_destino, progress, progress_text, snack_bar, page):
    try:
        imagenes = [f for f in os.listdir(carpeta_origen) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        total = len(imagenes)
        progress.value = 0
        progress.visible = True  # Mostrar la barra de progreso al comenzar
        progress_text.visible = True  # Mostrar el texto "Progreso:" al comenzar
        page.update()

        for index, filename in enumerate(imagenes, start=1):
            input_image_path = os.path.join(carpeta_origen, filename)
            output_image_path = os.path.join(
                carpeta_destino,
                filename.replace(".png", "_sinfondo.png").replace(".jpg", "_sinfondo.png").replace(".jpeg", "_sinfondo.png")
            )
            eliminar_fondo(input_image_path, output_image_path)

            # Actualiza el progreso
            progress.value = index / total
            snack_bar.content.value = f"Procesando {index}/{total}: {filename}"
            snack_bar.open = True
            page.update()

        snack_bar.content.value = f"Fondo eliminado de todas las imágenes en {carpeta_origen}"
        snack_bar.open = True
        progress.visible = False  # Ocultar la barra de progreso al terminar
        progress_text.visible = False  # Ocultar el texto "Progreso:" al terminar
        page.update()
    except Exception as e:
        snack_bar.content.value = f"Error al procesar la carpeta: {e}"
        snack_bar.open = True
        progress.visible = False  # Ocultar la barra de progreso en caso de error
        progress_text.visible = False  # Ocultar el texto "Progreso:" en caso de error
        page.update()

# Función para abrir la carpeta de destino en el sistema operativo
def abrir_carpeta_destino(carpeta):
    try:
        if platform.system() == "Windows":
            subprocess.run(["explorer", carpeta])
        elif platform.system() == "Linux":
            subprocess.run(["xdg-open", carpeta])
        else:
            print("Sistema operativo no soportado")
    except Exception as e:
        print(f"Error al abrir la carpeta: {e}")
