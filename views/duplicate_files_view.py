import flet as ft

def duplicate_files_view(page, state, folder_picker, result_text, delete_all_button, selected_dir_text, duplicates_list):
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Eliminar Archivos Duplicados",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200,
                ),
                margin=ft.margin.only(bottom=20),
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Seleccionar Carpeta",
                    icon=ft.Icons.FOLDER_OPEN,
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.BLUE_900,
                    on_click=lambda _: folder_picker.get_directory_path(),
                ),
                delete_all_button,
            ]),
            ft.Container(
                content=selected_dir_text,
                margin=ft.margin.only(top=10, bottom=10),
            ),
            result_text,
            ft.Container(
                content=duplicates_list,
                border=ft.border.all(2, ft.Colors.BLUE_500),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.Colors.GREY_800,
                expand=True,
            ),
        ]),
        padding=30,
        expand=True,
    )