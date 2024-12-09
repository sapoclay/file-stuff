import flet as ft
from functions.functions_rename_files import seleccionar_carpeta, renombrar_archivos

def rename_files_view(page, state, folder_picker, snack_bar, carpeta_text):
    # Campo de entrada para la plantilla de nombres
    name_template_field = ft.TextField(label="Plantilla de nombre (usa ### para el contador)")

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
                on_click=lambda _: seleccionar_carpeta(folder_picker),
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
                on_click=lambda _: renombrar_archivos(state, name_template_field, snack_bar, page),
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