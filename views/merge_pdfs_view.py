import flet as ft
from state_controls import pdf_dir
from functionalities.merge_pdf import merge_pdf
import os
import subprocess

def merge_pdfs_view(page, state, folder_picker, snack_bar):
    # Campo para ingresar el nombre del archivo de salida
    output_name_field = ft.TextField(
        label="Nombre del archivo fusionado (sin extensión)",
        value="merged_file",
        width=300
    )

    def seleccionar_carpeta(e):
        folder_picker.get_directory_path()

    def fusionar_archivos(e):

        # Verificar si se seleccionó una carpeta
        if not state.get("merge_pdfs"):
            snack_bar.content.value = "Selecciona una carpeta con archivos PDF primero."
            snack_bar.open = True
            page.update()
            return

        # Verificar si hay archivos PDF en la carpeta seleccionada
        input_folder = state["merge_pdfs"]
        pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

        if not pdf_files:
            snack_bar.content.value = "No se encontraron archivos PDF en la carpeta seleccionada."
            snack_bar.open = True
            page.update()
            return

        # Verificar si se ingresó un nombre para el archivo de salida
        output_name = output_name_field.value.strip()
        if not output_name:
            snack_bar.content.value = "Especifica un nombre para el archivo fusionado."
            snack_bar.open = True
            page.update()
            return

         # Generar la ruta completa del archivo de salida
        input_folder = state["merge_pdfs"]
        output_file = os.path.join(input_folder, f"{output_name}.pdf")

        try:
            # Llamar a la función de fusión
            merge_pdf(input_folder, output_file)
            
            # Mostrar resultado en el snackbar
            snack_bar.content.value = f"PDFs fusionados correctamente como '{output_name}.pdf' en:\n{input_folder}"
            snack_bar.open = True
            page.update()
            # Hacer visible el botón para abrir la carpeta
            abrir_carpeta_button.data = input_folder  # Guarda la carpeta en el botón
            abrir_carpeta_button.visible = True
            abrir_carpeta_button.update()
        except Exception as ex:
            snack_bar.content.value = f"Error durante la fusión: {str(ex)}"
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
                    "Fusionar PDFs",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.ElevatedButton(
                "Seleccionar Carpeta",
                icon=ft.Icons.FOLDER_OPEN,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_900,
                on_click=seleccionar_carpeta
            ),
            pdf_dir,  # Mostrar la carpeta seleccionada
            output_name_field,  # Campo para escribir el nombre del archivo
            ft.ElevatedButton(
                "Fusionar PDFs",
                icon=ft.Icons.MERGE_TYPE,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_900,
                on_click=fusionar_archivos
            ),
            abrir_carpeta_button,  # Botón para abrir la carpeta de salida
        ]),
        padding=30,
        expand=True
    )
