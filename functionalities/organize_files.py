import os
import shutil

def organize_folder(folder):
    file_types = {
        'Imagenes': ['.jpeg', '.jpg', '.png', '.gif', '.webp'],
        'Vídeos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Documentos': ['.pdf', '.docx', '.txt', '.m3u8', '.m3u'],
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