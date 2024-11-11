import flet as ft
from state import selected_dir_text, state, delete_all_button, organize_dir_text, organize_result_text, result_text, duplicates_list
from configtheme import configure_theme
from menu import build_navigation_rail  # Importamos la función
from views import create_duplicate_file_view, create_organize_files_view  # Importamos las vistas
from borrar_archivos_duplicados import find_duplicates
from deletes import delete_duplicate
from oraganizar_archivos import organize_folder

# Mueve scan_directory fuera de main
def scan_directory(directory):
    duplicates_list.controls.clear()
    state["current_duplicates"] = find_duplicates(directory)
    
    if not state["current_duplicates"]:
        result_text.value  = "No se encontraron archivos duplicados"
        result_text.color = ft.colors.GREEN_400
        delete_all_button.visible = False  # Oculta el botón si no hay duplicados
    else:
        result_text.value  = f"Se encontraron {len(state['current_duplicates'])} archivos duplicados"
        result_text.color = ft.colors.ORANGE_400
        # Volvemos visible el botón eliminar TODOS
        delete_all_button.visible = True
        # Listamos los archivos duplicados encontrados
        for dup_file, original in state["current_duplicates"]:
            dup_row = ft.Row([
                    ft.Text(
                    value=f"Duplicado: {dup_file}\nOriginal: {original}",
                    size=12,
                    expand=True,
                    color=ft.colors.WHITE
                ),
                ft.ElevatedButton(
                    "Eliminar",
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.RED_900,
                    on_click=lambda e , path=dup_file: delete_duplicate(path)
                )
            ])
            duplicates_list.controls.append(dup_row)
    duplicates_list.update()
    result_text.update()
    delete_all_button.update()

# Mueve organize_directory fuera de main
def organize_directory(directory):
    try:
        organize_folder(directory)
        organize_result_text.value = "Archivos organizados de forma exitosa!!"
        organize_result_text.color = ft.colors.GREEN_400
    except Exception as e:
        organize_result_text.value = f"Se ha producido un error al organizar los archivos: {str(e)}"
        organize_result_text.color = ft.colors.RED_400
    organize_result_text.update()

def handle_folder_picker(e: ft.FilePickerResultEvent):
    if e.path:
        if state["current_view"] == "duplicates":
            selected_dir_text.value = f"Carpeta seleccionada: {e.path}"
            selected_dir_text.update()
            scan_directory(e.path)  # Ahora scan_directory es accesible
        elif state["current_view"] == "organize":
            organize_dir_text.value = f"Carpeta seleccionada: {e.path}"
            organize_dir_text.update()
            organize_directory(e.path)  # Ahora organize_directory es accesible

def main(page: ft.Page):
    # Configuración de la ventana principal
    page.title = "Tareas básicas"
    page.window.width = 1000
    page.window.height = 700
    page.padding = 0
    page.bgcolor = ft.colors.BACKGROUND
    page.theme_mode = ft.ThemeMode.DARK
    
    page.theme = configure_theme()
    
    # Configurar el selector de carpetas
    folder_picker = ft.FilePicker(on_result=handle_folder_picker)
    page.overlay.append(folder_picker)
    
    # Vista de archivos duplicados
    duplicate_file_view = create_duplicate_file_view(folder_picker, scan_directory)
    
    # Vista de organizar archivos
    organize_files_view = create_organize_files_view(folder_picker, organize_directory)
    
    content_area = ft.Container(
        content=duplicate_file_view,
        expand=True,
    )
    
    # Añadir el rail con su configuración desde el archivo menu.py
    rail = build_navigation_rail(content_area, duplicate_file_view, organize_files_view)
    
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                content_area,
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
