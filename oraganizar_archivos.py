import os
import shutil

def organize_folder(folder):
    file_types = {
        'Imagenes': ['.jpeg', '.jpg', '.png', '.gif'],
        'Vídeos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Documentos': ['.pdf', 'docx', '.txt', '.m3u'],
        'Cálculo': ['.xlsx', '.csv'],
        'Comprimidos': ['.zip', '.rar', '.gz']
    }
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower() #almacenamos la extensión del archivo en minúsculas
            for folder_name, extensions in file_types.items():
                if extension in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True) # Creamos la carpeta de la categoría encontrada
                    shutil.move(file_path, os.path.join(target_folder, filename)) #movemos el archivo
                    print(f'Archivo {filename} movido a {folder_name}')