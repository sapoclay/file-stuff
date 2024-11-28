import flet as ft
from functionalities.delete_duplicates import find_duplicates, delete_file

# Función para eliminar UN SOLO archivo duplicado
def delete_duplicate(filepath):
    if delete_file(filepath):
        result_text.value = f"Archivo eliminado: {filepath}"
        result_text.color = ft.colors.GREEN_500
        for control in duplicates_list.controls[:]:
            if filepath in control.controls[0].value:
                duplicates_list.controls.remove(control)
        state["current_duplicates"] = [(dup, orig) for dup, orig in state["current_duplicates"] if dup != filepath]
        if not state["current_duplicates"]:
            delete_all_button.visible = False
    else:
        result_text.value = f"Error al eliminar: {filepath}"
        result_text.color = ft.colors.RED_500

    duplicates_list.update()
    result_text.update()
    delete_all_button.update()

def delete_all_duplicates():
    # Lógica para eliminar todos los archivos duplicados
    pass

def scan_directory(directory, state, result_text, delete_all_button, duplicates_list):
    # Escanea el directorio en busca de archivos duplicados
    duplicates_list.controls.clear()
    state["current_duplicates"] = find_duplicates(directory)

    if not state["current_duplicates"]:
        result_text.value = "No se han encontrado archivos duplicados"
        result_text.color = ft.colors.GREEN_500
        delete_all_button.visible = False
    else:
        result_text.value = f"Se encontraron {len(state['current_duplicates'])} archivos duplicados"
        result_text.color = ft.colors.ORANGE_500
        delete_all_button.visible = True

        for dup_file, original in state["current_duplicates"]:
            dup_row = ft.Row([
                ft.Text(
                    f"Duplicado {dup_file}\nOriginal: {original}",
                    size=12,
                    expand=True,
                    color=ft.colors.BLUE_200
                ),
                ft.ElevatedButton(
                    "Eliminar",
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.RED_900,
                    on_click=lambda e, path=dup_file: delete_duplicate(path)
                )
            ])
            duplicates_list.controls.append(dup_row)
    duplicates_list.update()
    result_text.update()
    delete_all_button.update()

def duplicate_files_view(page: ft.Page, state, result_text, delete_all_button, duplicates_list):
    # Vista para eliminar archivos duplicados
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Eliminar Archivos Duplicados",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Seleccionar Carpeta",
                    icon=ft.Icons.FOLDER_OPEN,
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.BLUE_900,
                    on_click=lambda _: page.open_folder_picker()  # Reemplaza con el manejo de la carpeta
                ),
                delete_all_button,
            ]),
            ft.Container(
                content=result_text,
                margin=ft.margin.only(top=10, bottom=10)
            ),
            ft.Container(
                content=duplicates_list,
                border=ft.border.all(2, ft.Colors.BLUE_500),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.Colors.GREY_800,
                expand=True
            )
        ]),
        padding=30,
        expand=True
    )