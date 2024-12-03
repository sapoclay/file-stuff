import os
import hashlib

"""
Este módulo proporciona funcionalidades para identificar y gestionar archivos duplicados en un directorio.

Funciones:
- hash_file(filename): Calcula y devuelve el hash MD5 de un archivo.
- find_duplicates(folder): Busca archivos duplicados en un directorio especificado y devuelve una lista con sus rutas.
- delete_file(filepath): Elimina un archivo dado y devuelve True si tiene éxito, o False en caso de error.

Dependencias:
- os: Para navegar por los directorios y gestionar archivos.
- hashlib: Para calcular el hash MD5 de los archivos.
"""

def hash_file(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(folder):
    hashes = {}
    duplicates = [] #lista
    
    for dirpath, _, filenames in os.walk(folder):
        # f es el nombre de cada archivo. Lo unimos a la ruta
        for f in filenames:
            full_path = os.path.join(dirpath, f)
            file_hash = hash_file(full_path)
            
            if file_hash in hashes:
                duplicates.append((full_path, hashes[file_hash]))
            else:
                hashes[file_hash] = full_path
    return duplicates

def delete_file(filepath):
    try:
        os.remove(filepath)
        return True
    except Exception as e:
        return False