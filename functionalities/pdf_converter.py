import pypandoc
import os

def convert_pdf(input_file, output_file):
    """
    Convierte un archivo PDF a .docx o .odt usando pypandoc.

    :param input_file: Ruta del archivo PDF de entrada.
    :param output_file: Ruta del archivo de salida con formato .docx o .odt.
    :return: Mensaje de éxito o error.
    """
    try:
        if not input_file.lower().endswith(".pdf"):
            return "Error: El archivo seleccionado no es un PDF."

        # Convertir usando pypandoc
        pypandoc.convert_file(input_file, 'odt' if output_file.endswith('.odt') else 'docx', outputfile=output_file)
        return f"Archivo convertido con éxito: {output_file}"
    except Exception as e:
        return f"Error al convertir el archivo: {str(e)}"
