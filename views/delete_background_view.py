import flet as ft
from functionalities.delete_background import eliminar_fondo_carpeta, abrir_carpeta_destino


def delete_background_view(page, state, folder_picker, snack_bar, carpeta_origen_text, carpeta_destino_text):
    progress = ft.ProgressBar(width=400, visible=False)
    progress_text = ft.Text("Progreso:", visible=False, color=ft.Colors.BLUE_200)

    # Función para seleccionar la carpeta de origen
    def seleccionar_carpeta_origen(e):
        state["selecting_destination"] = False
        folder_picker.get_directory_path()

    # Función para seleccionar la carpeta de destino
    def seleccionar_carpeta_destino(e):
        state["selecting_destination"] = True
        folder_picker.get_directory_path()

    # Procesar imágenes para eliminar el fondo
    def procesar_imagenes(e):
        if not state.get("input_folder"):  # Validar si la carpeta de origen no está seleccionada
            snack_bar.content.value = "Error: No se ha seleccionado una carpeta de origen."
            snack_bar.open = True
            page.update()
            return
        if not state.get("output_folder"):  # Validar si la carpeta de destino no está seleccionada
            snack_bar.content.value = "Error: No se ha seleccionado una carpeta de destino."
            snack_bar.open = True
            page.update()
            return

        try:
            eliminar_fondo_carpeta(
                state["input_folder"], 
                state["output_folder"], 
                progress, 
                progress_text, 
                snack_bar, 
                page
            )
        except Exception as ex:
            snack_bar.content.value = f"Error al eliminar el fondo: {ex}"
            snack_bar.open = True
            page.update()

    # Abrir carpeta de destino en el sistema operativo
    def abrir_destino(e):
        if state.get("output_folder"):  # Validar si la carpeta de destino está seleccionada
            try:
                abrir_carpeta_destino(state["output_folder"])
            except Exception as ex:
                snack_bar.content.value = f"Error al abrir la carpeta de destino: {ex}"
                snack_bar.open = True
                page.update()
        else:
            snack_bar.content.value = "Error: No se ha seleccionado una carpeta de destino."
            snack_bar.open = True
            page.update()

    # Retorna el contenedor con los controles de la vista
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Eliminar Fondo de Imágenes",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.ElevatedButton(
                "Seleccionar Carpeta de Origen",
                icon=ft.Icons.FOLDER_OPEN,
                on_click=seleccionar_carpeta_origen,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_900
            ),
            carpeta_origen_text,  # Control de texto para carpeta de origen
            ft.ElevatedButton(
                "Seleccionar Carpeta de Destino",
                icon=ft.Icons.FOLDER_OPEN,
                on_click=seleccionar_carpeta_destino,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_900
            ),
            carpeta_destino_text,  # Control de texto para carpeta de destino
            ft.Row([
                ft.ElevatedButton(
                    "Eliminar Fondo",
                    icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.RED_700,
                    on_click=procesar_imagenes
                ),
                ft.ElevatedButton(
                    "Abrir Carpeta de Destino",
                    icon=ft.Icons.FOLDER,
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.GREEN_700,
                    on_click=abrir_destino
                ),
            ], spacing=10),
            progress_text,
            progress,
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Información:",
                        size=14,
                        color=ft.Colors.BLUE_200,
                    ),
                    ft.Text("- Formatos soportados: .png, .jpeg y .jpg", size=14),
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
