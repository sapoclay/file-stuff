# views.py
import flet as ft
from borrar_archivos_duplicados import find_duplicates
from deletes import delete_duplicate
from oraganizar_archivos import organize_folder
from state import selected_dir_text, state, delete_all_button, organize_dir_text, organize_result_text, result_text, duplicates_list

def create_duplicate_file_view(folder_picker, scan_directory):
    # Vista de archivos duplicados
    duplicate_file_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    value="Eliminar archivos duplicados",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE_200
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Seleccionar Carpeta",
                    icon=ft.icons.FOLDER_OPEN,
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLUE_900,
                    on_click=lambda _: folder_picker.get_directory_path()
                ),
                delete_all_button,
            ]),
            ft.Container(
                content=selected_dir_text,
                margin=ft.margin.only(top=10, bottom=10)
            ),
            result_text,
            ft.Container(
                content=duplicates_list,
                border=ft.border.all(2, ft.colors.PURPLE_900),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.colors.GREY_800,
                expand=True
            )
        ]),
        padding=30,
        expand=True
    )
    return duplicate_file_view

def create_organize_files_view(folder_picker, organize_directory):
    # Vista de organizar archivos
    organize_files_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Organizar archivos por TIPO",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE_200,
                ),
                margin=ft.margin.only(bottom=20)  
            ),
            ft.ElevatedButton(
                "Seleccionar Carpeta",
                icon=ft.icons.FOLDER_OPEN,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_900,
                on_click=lambda _: folder_picker.get_directory_path()
            ),
            ft.Container(
                content=organize_dir_text,
                margin=ft.margin.only(top=10, bottom=10)
            ),
            organize_result_text,
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Los archivos serán organizados en las siguientes carpetas",
                        size=14,
                        color=ft.colors.BLUE_200
                    ),
                    ft.Text("Imágenes (.jpeg, .jpg, .png, .gif)", size=14),
                    ft.Text("Vídeos (.mp4, .mkv, .avi, .mov)", size=14),
                    ft.Text("Documentos (.pdf, .docx, .txt, .m3u)", size=14),
                    ft.Text("Cálculo (.xlsx, .csv)", size=14),
                    ft.Text("Comprimidos (.zip, .rar, .gz)", size=14),
                ]),
                border=ft.border.all(2, ft.colors.BLUE_400),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.colors.GREY_800,
            )
        ]),
        padding=30,
        expand=True
    )
    return organize_files_view
