import flet as ft

def convert_images_view(
    page,
    state,
    file_picker,
    convert_input_text,
    format_dropdown,
    convert_result_text,
    convert_image_function
):
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Convertir Formato de Imagen",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200,
                ),
                margin=ft.margin.only(bottom=20),
            ),
            ft.ElevatedButton(
                "Seleccionar Imagen",
                icon=ft.Icons.IMAGE,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_900,
                on_click=lambda _: file_picker.pick_files(),
            ),
            ft.Container(
                content=convert_input_text,
                margin=ft.margin.only(top=10, bottom=10),
            ),
            format_dropdown,
            ft.Container(
                margin=ft.margin.only(top=10),
                content=ft.ElevatedButton(
                    "Convertir Imagen",
                    icon=ft.Icons.TRANSFORM,
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.BLUE_900,
                    on_click=lambda _: convert_image_function(
                        state, convert_input_text, format_dropdown, convert_result_text
                    ),
                ),
            ),
            convert_result_text,
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Información:",
                        size=14,
                        color=ft.Colors.BLUE_200,
                    ),
                    ft.Text("- Formatos soportados: PNG, JPEG, WEBP, BMP, GIF", size=14),
                    ft.Text("- La imagen original no será modificada", size=14),
                    ft.Text("- La imagen convertida se guardará en la misma carpeta que la original", size=14),
                    ft.Text("- Al convertir a JPEG, las imágenes con transparencia se convertirán a fondo blanco", size=14),
                ]),
                border=ft.border.all(2, ft.Colors.BLUE_500),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.Colors.GREY_800,
            ),
        ]),
        padding=30,
        expand=True,
    )
