import os
import hashlib


def hash_file(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file: # Abrimos y leemos el archivo
        while chunk := file.read(8192): # Carga de 8 en 8 Kb para no sobrecargar la memoria.
            h.update(chunk) # Acumulamos el hash en h
        return h.hexdigest() # Devuelve un hash hexadecimal
    
def find_duplicates(folder):
    hashes = {} # Diccionario 
    duplicates = [] # Lista para duplicados
    for dirpath, _, filenames in os.walk(folder):
        for a in filenames:
            full_path = os.path.join(dirpath, a) # join une la ruta de los archivos con su nombre
            file_hash = hash_file(full_path)
            
            if file_hash in hashes: # Si el hash está en el diccionario hashes
                duplicates.append((full_path, hashes[file_hash]))
            else: # Si el hash no está en el diccionario, se añade
                hashes[file_hash] = full_path
                
    return duplicates

def delete_file(filepath):
    try:
        os.remove(filepath)
        return True
    except Exception as e:
        return False
    
