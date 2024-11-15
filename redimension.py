from PIL import Image, UnidentifiedImageError
import os

def barch_resize(folder_in, folder_out, width, height):
    # Extensiones válidas para imágenes
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}
    
    # Listas para archivos redimensionados y con errores
    resized_files = []
    error_files = []

    for filename in os.listdir(folder_in):
        # Verificar si el archivo tiene una extensión válida
        if not any(filename.lower().endswith(ext) for ext in valid_extensions):
            print(f"Archivo {filename} omitido: no tiene una extensión válida.")
            error_files.append(filename)
            continue

        input_path = os.path.join(folder_in, filename)
        output_path = os.path.join(folder_out, filename)

        try:
            # Intentar abrir y redimensionar la imagen
            with Image.open(input_path) as img:
                resized_img = img.resize((width, height))
                resized_img.save(output_path)
                print(f"Imagen {filename} redimensionada correctamente.")
                resized_files.append(filename)  # Añadir a la lista de archivos redimensionados
        except (UnidentifiedImageError, IOError) as e:
            print(f"Archivo {filename} no es una imagen válida o no se pudo procesar: {e}")
            error_files.append(filename)  # Añadir a la lista de archivos con errores

    # Retornar las listas de archivos redimensionados y con errores
    return resized_files, error_files
