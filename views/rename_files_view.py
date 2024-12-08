import flet as ft
from functionalities.rename_all_files import bulk_rename_files

def rename_files_view(page, state, folder_picker, snack_bar, carpeta_text):
    name_template_field = ft.TextField(label="Plantilla de nombre (usa ### para el contador)")

    # Función para seleccionar la carpeta de origen
    def seleccionar_carpeta(e):
        folder_picker.get_directory_path()

    # Función para renombrar los archivos
    def renombrar_archivos(e):
        if not state.get("rename_folder"):
            snack_bar.content.value = "Selecciona una carpeta primero."
            snack_bar.open = True
            page.update()
            return

        if not name_template_field.value:
            snack_bar.content.value = "Especifica una plantilla de nombre."
            snack_bar.open = True
            page.update()
            return

        # Verificar si la plantilla contiene '###'
        if '###' not in name_template_field.value:
            snack_bar.content.value = "Error: La plantilla debe contener '###' para indicar la posición del contador."
            snack_bar.open = True
            page.update()
            return

        # Llamar a la función para renombrar archivos
        result = bulk_rename_files(state["rename_folder"], name_template_field.value, snack_bar)
        if isinstance(result, list):
            snack_bar.content.value = f"Archivos renombrados correctamente. Total: {len(result)}"
        else:
            snack_bar.content.value = f"Error: {result}"
        snack_bar.open = True
        page.update()

    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Renombrar Archivos en Masa",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.ElevatedButton(
                "Seleccionar Carpeta",
                icon=ft.Icons.FOLDER_OPEN,
                on_click=seleccionar_carpeta,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_900
            ),
            carpeta_text,  # Mostrar la carpeta seleccionada
            name_template_field,
            ft.ElevatedButton(
                "Renombrar Archivos",
                icon=ft.Icons.DRIVE_FILE_RENAME_OUTLINE,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.GREEN_700,
                on_click=renombrar_archivos
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Información:",
                        size=14,
                        color=ft.Colors.BLUE_200,
                    ),
                    ft.Text("- Es necesario añadir la extensión para los archivos", size=14),
                    ft.Text("- Se va a modificar el nombre de todos los archivos", size=14),
                    ft.Text("- Solo es posible seleccionar una carpeta, NO archivos individuales", size=14),
                ]),
                border=ft.border.all(2, ft.Colors.BLUE_500),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.Colors.GREY_800,
            ),
        ]),
        padding=30,
        expand=True
    )
