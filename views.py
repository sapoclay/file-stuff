import os
import flet as ft
from borrar_archivos_duplicados import find_duplicates
from deletes import delete_duplicate
from oraganizar_archivos import organize_folder
from renameall import bulk_rename_files
from redimension import barch_resize
from state import selected_dir_text, state, delete_all_button, organize_dir_text, organize_result_text, result_text, duplicates_list, selected_bulk_text, resize_input_text, resize_output_text, resize_result_text
from styles_views import create_title, create_elevated_button, folder_selection_text_style, result_text_style

# Importa los estilos
from styles_views import create_title, create_container_with_padding, create_elevated_button, container_border_style, title_text_style

def create_duplicate_file_view(folder_picker, scan_directory):
    duplicate_file_view = create_container_with_padding(
        ft.Column([
            create_title("Eliminar archivos duplicados"),  # Usa el título común
            ft.Row([
                create_elevated_button(
                    "Seleccionar Carpeta",
                    ft.icons.FOLDER_OPEN,
                    lambda _: folder_picker.get_directory_path()
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
                **container_border_style(),  # Usa el estilo de contenedor con borde
                expand=True
            )
        ])
    )
    return duplicate_file_view

def create_organize_files_view(folder_picker, organize_directory):
    organize_files_view = create_container_with_padding(
        ft.Column([
            create_title("Organizar archivos por TIPO"),  # Usa el título común
            create_elevated_button(
                "Seleccionar Carpeta",
                ft.icons.FOLDER_OPEN,
                lambda _: folder_picker.get_directory_path()
            ),
            ft.Container(
                content=organize_dir_text,
                margin=ft.margin.only(top=10, bottom=10)
            ),
            organize_result_text,
            ft.Container(
                content=ft.Column([
                    ft.Text("Los archivos serán organizados en las siguientes carpetas", size=14, color=ft.colors.BLUE_200),
                    ft.Text("Imágenes (.jpeg, .jpg, .png, .gif)", size=14),
                    ft.Text("Vídeos (.mp4, .mkv, .avi, .mov)", size=14),
                    ft.Text("Documentos (.pdf, .docx, .txt, .m3u)", size=14),
                    ft.Text("Cálculo (.xlsx, .csv)", size=14),
                    ft.Text("Comprimidos (.zip, .rar, .gz)", size=14),
                ]),
                **container_border_style(),  # Usa el estilo de contenedor con borde
            )
        ])
    )
    return organize_files_view

def create_bulk_rename_view(page, folder_picker, rename_directory):
    name_template_input = ft.TextField(label="Plantilla de nombre", hint_text="Ejemplo: archivo_###.txt")
    rename_result_text = ft.Text(value="", size=12, color=ft.colors.GREEN_400)
    renamed_files_list = ft.Column([])  # Lista para mostrar los archivos renombrados
    
    selected_dir_text_container = ft.Container(
        content=selected_bulk_text,
        padding=ft.padding.all(10)
    )
    
    def on_rename_click(e):
        if "selected_directory" not in state or not state["selected_directory"]:
            rename_result_text.value = "Por favor, selecciona una carpeta primero."
            rename_result_text.color = ft.colors.RED_400
            rename_result_text.update()
            return  # Detener el proceso si no hay carpeta seleccionada

        def on_confirm_yes(e):
            renamed_files = rename_directory(name_template_input.value)
            renamed_files_list.controls.clear()  # Limpiar la lista previa

            if renamed_files:
                for file in renamed_files:
                    renamed_files_list.controls.append(ft.Text(file, color=ft.colors.GREEN_400))
                rename_result_text.value = "Renombrado completado con éxito."
                rename_result_text.color = ft.colors.GREEN_400
            else:
                rename_result_text.value = "No se encontraron archivos para renombrar."
                rename_result_text.color = ft.colors.RED_400

            renamed_files_list.update()
            rename_result_text.update()
            confirm_dialog.open = False
            page.update()

        def on_confirm_no(e):
            confirm_dialog.open = False
            page.update()

        confirm_dialog = ft.AlertDialog(
            title=ft.Text("Confirmación"),
            content=ft.Text("¿Está seguro de renombrar los archivos?"),
            actions=[
                ft.TextButton("Sí", on_click=on_confirm_yes),
                ft.TextButton("No", on_click=on_confirm_no)
            ]
        )
        
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    return create_container_with_padding(
        ft.Column([
            create_title("Renombrar archivos en grupo"),  # Usa el título común
            create_elevated_button(
                "Seleccionar carpeta",
                ft.icons.FOLDER,
                lambda _: folder_picker.get_directory_path(),
            ),
            selected_dir_text_container,
            name_template_input,
            create_elevated_button(
                "Renombrar archivos",
                ft.icons.DRIVE_FILE_RENAME_OUTLINE,
                on_rename_click
            ),
            rename_result_text,
            renamed_files_list
        ])
    )


def create_resize_image_view(folder_picker, resize_images_func):
    # Variables de estado para carpetas de entrada y salida
    input_folder = ""
    output_folder = ""

    # Texto inicial para las carpetas de entrada y salida
    initial_input_text = "Seleccione una carpeta de entrada"
    initial_output_text = "Seleccione una carpeta de salida"

    # Texto de selección de carpeta de entrada y salida (usando el estilo de styles_views)
    resize_input_text = folder_selection_text_style(initial_input_text)
    resize_output_text = folder_selection_text_style(initial_output_text)

    # Configuración de selección de carpetas
    def pick_input_folder(e):
        state["selecting_resize_output"] = False
        folder_picker.get_directory_path()

    def pick_output_folder(e):
        state["selecting_resize_output"] = True
        folder_picker.get_directory_path()

    def handle_folder_selection(e):
        if state.get("selecting_resize_output", False):
            state["resize_output_folder"] = e.path
            resize_output_text.value = f"Carpeta de salida: {e.path}" if e.path else initial_output_text
            resize_output_text.update()
        else:
            state["resize_input_folder"] = e.path
            resize_input_text.value = f"Carpeta de entrada: {e.path}" if e.path else initial_input_text
            resize_input_text.update()

    folder_picker.on_result = handle_folder_selection

    # Campos de entrada para ancho y alto
    width_input = ft.TextField(label="Ancho (px)", width=100)
    height_input = ft.TextField(label="Alto (px)", width=100)

    # Contenedores de resultados para archivos redimensionados y con errores
    resized_files_list = ft.Column(scroll=ft.ScrollMode.AUTO, height=150)
    error_files_list = ft.Column(scroll=ft.ScrollMode.AUTO, height=150)

    # Texto de resultado general (usando el estilo de result_text_style de styles_views)
    resize_result_text = result_text_style()

    def on_resize_click(e):
        # Validación de selección de carpetas
        if not state.get("resize_input_folder"):
            resize_result_text.value = "Seleccione una carpeta de entrada."
            resize_result_text.color = ft.colors.RED_400
            resize_result_text.update()
            return

        if not state.get("resize_output_folder"):
            resize_result_text.value = "Seleccione una carpeta de salida."
            resize_result_text.color = ft.colors.RED_400
            resize_result_text.update()
            return

        # Validación de dimensiones
        try:
            width = int(width_input.value)
            height = int(height_input.value)
            if width <= 0 or height <= 0:
                raise ValueError("Las dimensiones deben ser mayores a cero.")
        except ValueError:
            resize_result_text.value = "Ingrese valores válidos para el ancho y alto."
            resize_result_text.color = ft.colors.RED_400
            resize_result_text.update()
            return

        # Llama a la función barch_resize
        resized_files, error_files = barch_resize(
            state["resize_input_folder"],
            state["resize_output_folder"],
            width,
            height
        )

        # Muestra los resultados en los contenedores de listas
        resized_files_list.controls.clear()
        error_files_list.controls.clear()

        for file in resized_files:
            resized_files_list.controls.append(ft.Text(f"✓ {file}", color=ft.colors.GREEN_400))

        # Filtrar sólo archivos para evitar mostrar directorios en la lista de errores
        for file in error_files:
            if os.path.isfile(os.path.join(state["resize_input_folder"], file)):
                error_files_list.controls.append(ft.Text(f"✗ {file}", color=ft.colors.RED_400))

        resized_files_list.update()
        error_files_list.update()

        # Mensaje final en resize_result_text
        resize_result_text.value = f"{len(resized_files)} imágenes redimensionadas correctamente."
        if error_files:
            resize_result_text.value += f" {len(error_files)} archivos tuvieron errores."
        resize_result_text.color = ft.colors.BLUE_400
        resize_result_text.update()

        # Restaurar los textos de selección de carpetas a su mensaje inicial
        resize_input_text.value = initial_input_text
        resize_output_text.value = initial_output_text
        resize_input_text.update()
        resize_output_text.update()

        # Limpiar las carpetas seleccionadas en el estado
        state["resize_input_folder"] = ""
        state["resize_output_folder"] = ""

    # Botón para redimensionar imágenes (usando create_elevated_button de styles_views)
    resize_button = create_elevated_button(
        "Redimensionar Imágenes", 
        ft.icons.PHOTO_SIZE_SELECT_SMALL, 
        on_resize_click
    )

    # Estructura completa de la vista de redimensionado
    resize_image_view = ft.Container(
        content=ft.Column([
            create_title("Redimensionar Imágenes"),
            # Crear el Row con dos Columnas
            ft.Row([
                ft.Column([
                    ft.ElevatedButton(
                        "Seleccionar carpeta de entrada",
                        icon=ft.icons.FOLDER_OPEN,
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE_900,
                        on_click=pick_input_folder
                    ),
                    resize_input_text,
                ], expand=True),  # Primera columna

                ft.Column([
                    ft.ElevatedButton(
                        "Seleccionar carpeta de salida",
                        icon=ft.icons.FOLDER_OPEN,
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE_900,
                        on_click=pick_output_folder
                    ),
                    resize_output_text,
                ], expand=True),  # Segunda columna
            ], spacing=10),  # Espacio entre las columnas
            ft.Divider(color=ft.colors.BLUE_200, thickness=2),  # Línea divisoria de color azul
            # Crear el Row con dos Columnas para ancho, alto y botón
            ft.Row([
                ft.Column([
                    width_input
                ], expand=True),  # Columna con ancho
                ft.Column([
                    height_input
                ], expand=True),  # Columna con ancho
                ft.Column([
                    resize_button
                ], expand=True),  # Columna con alto
            ], spacing=10),  # Espacio entre las columnas

            resize_result_text,
            ft.Divider(color=ft.colors.BLUE_200, thickness=2),  # Línea divisoria de color azul
            ft.Row([
                ft.Column([
                    ft.Text("Archivos redimensionados:", color=ft.colors.GREEN_400),
                    resized_files_list,
                ], expand=True),
                ft.Column([
                    ft.Text("Archivos con errores:", color=ft.colors.RED_400),
                    error_files_list,
                ], expand=True),
            ], spacing=10),  # Reduce el espacio entre las columnas
        ], spacing=15),  # Reduce el espacio entre los elementos en la columna principal
        padding=30,
        expand=True
    )

    return resize_image_view
