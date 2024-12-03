import flet as ft
from state_controls import organize_dir_text, selected_dir_text
from functions.functions_duplicate_files import scan_directory
from functions.functions_organize_files import organize_directory

def select_input_folder(state, folder_picker):
    # Configura la selección de entrada
    state["selecting_resize_output"] = False
    folder_picker.get_directory_path()

def select_output_folder(state, folder_picker):
    # Configura la selección de salida
    state["selecting_resize_output"] = True
    folder_picker.get_directory_path()

def handle_folder_picker(
    e, state, page, selected_dir_text, scan_directory, organize_directory,
    resize_input_text, resize_output_text, folder_picker, result_text, delete_all_button, duplicates_list, organize_result_text
):
    if e.path:
        if state["current_view"] == "duplicates":
            # Actualizar texto de la carpeta seleccionada
            selected_dir_text.value = f"Carpeta seleccionada: {e.path}"
            selected_dir_text.update()
            # Llamar a scan_directory con los parámetros necesarios
            scan_directory(e.path, state, result_text, delete_all_button, duplicates_list)
        elif state["current_view"] == "organize":
            organize_dir_text.value = f"Carpeta seleccionada: {e.path}"
            organize_dir_text.update()
            # Incluir organize_result_text en la llamada
            organize_directory(e.path, organize_result_text)
        elif state["current_view"] == "resize":
            if state["selecting_resize_output"]:
                # Guardar carpeta de salida
                state["resize_output_folder"] = e.path
                resize_output_text.value = f"Carpeta de salida: {e.path}"
                resize_output_text.update()
            else:
                # Guardar carpeta de entrada
                state["resize_input_folder"] = e.path
                resize_input_text.value = f"Carpeta de entrada: {e.path}"
                resize_input_text.update()
