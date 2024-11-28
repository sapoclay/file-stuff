import os
from PIL import Image

def convert_img(ruta_entrada, formato_salida):
    """ 
    Convierte una imagen al formato de salida

    Args:
        ruta_entrada (str): Ruta del archivo de imagen original
        formato_salida (str): formato deseado (png, jpeg, webp, bmp, gif ....)
    """
    
    try:
        # Obtener el nombre del archivo sin extensión
        nombre_base = os.path.splitext(ruta_entrada)[0]
        
        #Abrir la imagen
        with Image.open(ruta_entrada) as img:
            # Si la imagen está en modo RGBA y queremos convertirla a JPEG, primero debemos convertirla a RGB
            if img.mode in ('RGBA', 'LA') and formato_salida.upper() == 'JPEG':
                img = img.convert('RGB')
                
            # Creamos el nombre del archivo de salida
            ruta_salida = f"{nombre_base}.{formato_salida.lower()}"
            
            # Guardamos la imagen en el nuevo formato dado. El formato de salida siempre en mayúsucula, por eso el upper
            img.save(ruta_salida, formato_salida.upper())
            
    except Exception as e:
        print(f"Error al convertir la imagen: {str(e)}")