import flet as ft
from state_controls import snack_bar, pdf_file_text, output_format_dropdown
from functions.functions_pdfto_docodx import convertir_pdf_a_docx
import os
import subprocess

def pdf_converter_view(page, state, folder_picker, snack_bar, output_format_dropdown):
    def seleccionar_pdf(e):
        folder_picker.pick_files(allowed_extensions=["pdf"])

    def convertir_archivo(e):
        if not state.get("pdf_file_path"):
            snack_bar.content.value = "Selecciona un archivo PDF primero."
            snack_bar.open = True
            page.update()
            return

        if not output_format_dropdown.value:
            snack_bar.content.value = "Selecciona un formato de salida."
            snack_bar.open = True
            page.update()
            return

        # Obtener el directorio del archivo original y el nombre base
        original_path = state["pdf_file_path"]
        original_dir = os.path.dirname(original_path)  # Ruta del directorio
        base_filename = os.path.splitext(os.path.basename(original_path))[0]  # Nombre sin extensión

        # Generar la ruta del archivo convertido (con extensión .docx)
        output_filename = f"{base_filename}.docx"
        output_path = os.path.join(original_dir, output_filename)

        # Conversión a DOCX
        archivo_generado = convertir_pdf_a_docx(original_path, output_path, snack_bar, page)

        # Verificar si la conversión fue exitosa
        if archivo_generado and os.path.exists(output_path):
            snack_bar.content.value = f"Archivo convertido exitosamente: {output_filename}"
            snack_bar.open = True
            abrir_carpeta_button.visible = True
            abrir_carpeta_button.data = original_dir  # Guardar la ruta del directorio en el botón
            abrir_carpeta_button.update()
        else:
            snack_bar.content.value = "Error: No se pudo convertir el archivo."
            snack_bar.open = True
            page.update()

    def abrir_carpeta(e):
        output_dir = e.control.data  # Recuperar la ruta de la carpeta desde el botón
        if output_dir:
            try:
                if os.name == "nt":  # Sistema operativo Windows
                    subprocess.run(["explorer", output_dir], check=True)
                elif os.name == "posix":  # Sistema operativo Linux
                    subprocess.run(["xdg-open", output_dir], check=True)
                else:
                    print(f"Error: Sistema operativo no soportado para abrir carpetas.")
            except Exception as ex:
                print(f"Error al intentar abrir la carpeta: {str(ex)}")


    # Botón para abrir la carpeta de salida
    abrir_carpeta_button = ft.ElevatedButton(
        "Abrir Carpeta de Salida",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=abrir_carpeta,
        visible=False,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.GREEN_700,
    )

    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Convertir PDF a DOCX",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.ElevatedButton(
                "Seleccionar Archivo PDF",
                icon=ft.Icons.PICTURE_AS_PDF,
                on_click=seleccionar_pdf
            ),
            pdf_file_text,  # Mostrar el texto del archivo seleccionado
            output_format_dropdown,
            ft.ElevatedButton(
                "Convertir Archivo",
                icon=ft.Icons.FORMAT_ALIGN_LEFT,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.GREEN_700,
                on_click=convertir_archivo
            ),
            abrir_carpeta_button,  # Botón para abrir la carpeta de salida
        ]),
        padding=30,
        expand=True
    )
