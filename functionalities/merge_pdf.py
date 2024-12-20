import os
from PyPDF2 import PdfMerger
from pathlib import Path

def merge_pdf(folder_input, file_output='merged_file.pdf'):
    """
    Fusionar todos los archivos PDF de una carpeta en un solo archivo PDF.
    
    :param folder_input: Carpeta con los archivos PDF a fusionar.
    :param file_output: Ruta del archivo PDF de salida.
    """
    try:
        # Creamos el merger
        merger = PdfMerger()
        
        # Verificar si la carpeta existe
        if not os.path.exists(folder_input):
            raise FileNotFoundError(f"La carpeta {folder_input} no existe.")
        
        # Obtener los archivos PDF de la carpeta
        pdfs = sorted(Path(folder_input).glob("*.pdf"))
        if not pdfs:
            raise ValueError(f"No se encontraron archivos PDF en la carpeta {folder_input}.")

        # Añadir cada PDF al merger
        for pdf in pdfs:
            merger.append(str(pdf))

        # Guardar el archivo fusionado
        merger.write(file_output)
        merger.close()
        print(f"Se ha creado el archivo {file_output} con éxito.")
        return file_output

    except Exception as e:
        raise RuntimeError(f"Error durante la creación del PDF único: {str(e)}")
