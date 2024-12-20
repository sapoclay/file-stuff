from pdf2docx import Converter
import os

def convertir_pdf_a_docx(pdf_file_path, output_path, snack_bar, page):
    """
    Convierte un archivo PDF a DOCX usando la librería pdf2docx.
    
    :param pdf_file_path: Ruta del archivo PDF.
    :param output_path: Ruta de salida para el archivo DOCX.
    :param snack_bar: Control para mostrar mensajes de error o éxito.
    :param page: Página de Flet donde se actualizan los controles.
    
    :return: Ruta del archivo DOCX generado o None en caso de error.
    """
    try:
        # Convertir PDF a DOCX
        cv = Converter(pdf_file_path)
        cv.convert(output_path, start=0, end=None, retain_layout=True)  # Convertir todo el documento con imágenes, tablas, etc.
        cv.close()  # Cerrar el conversor
        
        # Verificar si el archivo DOCX se generó correctamente
        if os.path.exists(output_path):
            snack_bar.content.value = f"Archivo convertido exitosamente: {output_path}"
            snack_bar.open = True
            page.update()
            return output_path
        else:
            snack_bar.content.value = "Error al generar el archivo DOCX."
            snack_bar.open = True
            page.update()
            return None
    except Exception as e:
        snack_bar.content.value = f"Error durante la conversión: {str(e)}"
        snack_bar.open = True
        page.update()
        return None
