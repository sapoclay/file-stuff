import flet as ft

def organize_files_view(page, state, folder_picker, organize_dir_text, organize_result_text):
    # Vista de organizar archivos
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Organizar archivos por TIPO",
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
                        "Los archivos serán organizados en las siguientes carpetas:",
                        size=14,
                        color=ft.Colors.BLUE_200
                    ),
                    ft.Text("- Imágenes (.jpeg, .jpg, .png, .gif, .webp, .xcf, .tiff, .ico)", size=14),
                    ft.Text("- Vídeos (.mp4, .mkv, .avi, .mov)", size=14),
                    ft.Text("- Audio (.mp3, .wav, .wma, .ogg)", size=14),
                    ft.Text("- Documentos (.pdf, .docx, .odt, .txt, .m3u8, .m3u, .json, .log)", size=14),
                    ft.Text("- Datasets (.xlsx, .csv)", size=14),
                    ft.Text("- Comprimidos (.zip, .rar, .gz)", size=14),
                    ft.Text("- Programas (.deb, .appImage, .exe, .msi, .snap, .flatpak)", size=14),
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