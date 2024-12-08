import os
import shutil

"""
Este módulo organiza los archivos de un directorio dado en subcarpetas basadas en sus extensiones.

Funciones:
- organize_folder(folder): Reorganiza los archivos en un directorio especificado según su tipo, moviéndolos a subcarpetas específicas.

Detalles:
- Los archivos se clasifican en categorías predefinidas como 'Imagenes', 'Vídeos', 'Documentos', etc., basándose en sus extensiones.
- Si la subcarpeta correspondiente no existe, se crea automáticamente.
- Los archivos se mueven a la subcarpeta apropiada utilizando `shutil.move`.

Dependencias:
- os: Para gestionar directorios y archivos.
- shutil: Para mover archivos entre directorios.

Parámetros:
- folder (str): Ruta al directorio que contiene los archivos a organizar.

Ejemplo:
>>> organize_folder('/ruta/a/mi/carpeta')
Archivo ejemplo.png movido a Imagenes
Archivo ejemplo.docx movido a Documentos
"""


def organize_folder(folder):
    # Tipos de archivos que se van a organizar
    file_types = {
        'Imagenes': ['.jpeg', '.jpg', '.png', '.gif', '.webp', '.xcf', '.tiff', '.ico'],
        'Vídeos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav', '.wma', '.ogg'],
        'Documentos': ['.pdf', '.docx', '.odt', '.txt', '.m3u8', '.m3u', '.json', '.log'],
        'Datasets': ['.xlsx', '.csv'],
        'Comprimidos': ['.zip', '.rar', '.gz'],
        'Programas': ['.deb', '.appImage', '.exe', '.msi', '.snap', '.flatpak'],
    }
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Archivo {filename} movido a {folder_name}")