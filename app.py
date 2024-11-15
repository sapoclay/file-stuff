import flet as ft
import os
from state import selected_dir_text, state, delete_all_button, organize_dir_text, organize_result_text, result_text, duplicates_list, selected_bulk_text, resize_input_text, resize_output_text, resize_result_text
from configtheme import configure_theme
from menu import build_navigation_rail  # Importamos la función
from views import create_duplicate_file_view, create_organize_files_view, create_bulk_rename_view, create_resize_image_view
from borrar_archivos_duplicados import find_duplicates
from deletes import delete_duplicate
from oraganizar_archivos import organize_folder
from renameall import bulk_rename_files
from redimension import barch_resize

# Nueva función para redimensionar imágenes
def resize_images(input_folder, output_folder, width, height, resize_result_text, error_files_text):
    # Llamar a la función barch_resize para redimensionar las imágenes
    resized_files, error_files = barch_resize(input_folder, output_folder, width, height)

    # Actualizar el texto de resultado según los archivos procesados
    if resized_files:
        resize_result_text.value = f"Archivos redimensionados: {', '.join(resized_files)}"
        resize_result_text.color = ft.colors.GREEN_400
    else:
        resize_result_text.value = "No se redimensionaron archivos."
        resize_result_text.color = ft.colors.RED_400

    # Actualizar los archivos con errores (si los hay)
    if error_files:
        error_files_text.value = f"Archivos con errores: {', '.join(error_files)}"
        error_files_text.color = ft.colors.RED_400
    else:
        error_files_text.value = "No hubo archivos con errores."
        error_files_text.color = ft.colors.GREEN_400

    # Actualizar los textos en la interfaz
    resize_result_text.update()
    error_files_text.update()

def rename_directory(name_template):
    # Lógica para renombrar archivos en base a una plantilla
    renamed_files = bulk_rename_files(state["selected_directory"], name_template)
    
    # Devuelve una lista de los archivos renombrados
    return renamed_files

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
        state["selected_directory"] = e.path  # Actualiza la ruta seleccionada

        # Asignar valor a selected_dir_text y verificar si está añadido a la página
        if state["current_view"] == "duplicates":
            selected_dir_text.value = f"Carpeta seleccionada: {e.path}"
            if selected_dir_text.page is not None:  # Verifica si está en la página
                selected_dir_text.update()
            scan_directory(e.path)  # Ejecuta la función de escaneo para duplicados

        elif state["current_view"] == "organize":
            organize_dir_text.value = f"Carpeta seleccionada: {e.path}"
            if organize_dir_text.page is not None:  # Verifica si está en la página
                organize_dir_text.update()
            organize_directory(e.path)  # Ejecuta la función para organizar archivos

        elif state["current_view"] == "rename":
            selected_bulk_text.value = f"Carpeta seleccionada para renombrar sus archivos: {e.path}"
            if selected_bulk_text.page is not None:  # Verifica si está en la página
                selected_bulk_text.update()


def main(page: ft.Page):
    # Configuración de la ventana principal
    page.title = "Files-Stuff"
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
    
    # Vista para renombrar archivos
    bulk_rename_view = create_bulk_rename_view(page, folder_picker, rename_directory)    
    
    # Vista para el redimensionado de imágenes
    resize_image_view = create_resize_image_view(folder_picker, resize_images)
    
    content_area = ft.Container(
        content=duplicate_file_view,
        expand=True,
    )
    
    # Añadir el rail con su configuración desde el archivo menu.py
    rail = build_navigation_rail(content_area, duplicate_file_view, organize_files_view, bulk_rename_view, resize_image_view)
        
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
