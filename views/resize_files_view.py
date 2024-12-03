import flet as ft
from functions.functions_resize_files import resize_images
from functions.functions_folder_picker import select_input_folder, select_output_folder
from state_controls import width_field, height_field, resize_result_text

def resize_files_view(
    page,
    state,
    folder_picker,
    resize_input_text,
    resize_output_text,
    resize_result_text,
    width_field,
    height_field
):
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Redimensionar Imágenes",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200,
                ),
                margin=ft.margin.only(bottom=20),
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Seleccionar Carpeta de Entrada",
                    icon=ft.Icons.FOLDER_OPEN,
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.BLUE_900,
                    on_click=lambda _: select_input_folder(state, folder_picker),
                ),
                ft.ElevatedButton(
                    "Seleccionar Carpeta de Salida",
                    icon=ft.Icons.FOLDER_OPEN,
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.BLUE_900,
                    on_click=lambda _: select_output_folder(state, folder_picker),
                ),
            ]),
            ft.Container(
                content=ft.Column([
                    resize_input_text,
                    resize_output_text,
                ]),
                margin=ft.margin.only(top=10, bottom=10),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Dimensiones de la imagen:",
                        size=14,
                        color=ft.Colors.BLUE_200,
                    ),
                    ft.Row([
                        width_field,
                        ft.Text("x", size=20),
                        height_field,
                        ft.Text(" píxeles", size=14),
                    ]),
                ]),
                margin=ft.margin.only(bottom=10),
            ),
            ft.ElevatedButton(
                "Redimensionar Imágenes",
                icon=ft.Icons.PHOTO_SIZE_SELECT_LARGE,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_900,
                on_click=lambda _: resize_images(state, resize_result_text, width_field, height_field),
            ),
            resize_result_text,
            ft.Container(
                content=ft.Column([
                    ft.Text("Información:", size=14, color=ft.Colors.BLUE_500),
                    ft.Text("- Se procesarán archivos .jpg, .jpeg, .png, .gif y .webp", size=14),
                    ft.Text("- Las imágenes originales no serán modificadas", size=14),
                    ft.Text("- Las imágenes redimensionadas se guardarán con el prefijo 'resized_'", size=14)
                ]),
                border=ft.border.all(2, ft.Colors.BLUE_500),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.Colors.GREY_800,
            )
        ]),
        padding=30,
        expand=True
    )