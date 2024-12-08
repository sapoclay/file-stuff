import flet as ft
from state_controls import organize_dir_text, selected_dir_text, carpeta_origen_text, carpeta_destino_text
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
    resize_input_text, resize_output_text, folder_picker, result_text,
    delete_all_button, duplicates_list, organize_result_text,
    carpeta_origen_text, carpeta_destino_text, organize_dir_text, carpeta_text
):
    if e.path:
        # Vista de archivos duplicados
        if state["current_view"] == "duplicates":
            state["selected_dir"] = e.path
            selected_dir_text.value = f"Carpeta seleccionada: {e.path}"
            if selected_dir_text.page:  # Verificar que selected_dir_text está en la página
                selected_dir_text.update()
            else:
                print("Error: selected_dir_text no está asociado a la página.")
            
            if duplicates_list.page:  # Verificar que duplicates_list está en la página
                scan_directory(e.path, state, result_text, delete_all_button, duplicates_list)
            else:
                print("Error: duplicates_list no está asociado a la página.")

        # Vista de organizar archivos
        elif state["current_view"] == "organize":
            state["organize_folder"] = e.path
            if hasattr(organize_dir_text, "_Control__page"):  # Validar si está asociado a la página
                organize_dir_text.value = f"Carpeta seleccionada: {e.path}"
                organize_dir_text.update()
            else:
                page.snack_bar.content.value = "Error: Control de texto no está agregado a la página."
                page.snack_bar.open = True
                page.update()
                print("Warning: organize_dir_text no está vinculado a la página.")
            organize_directory(e.path, organize_result_text)
        
        # Vista de redimensionar imágenes
        elif state["current_view"] == "resize":
            if state["selecting_resize_output"]:
                state["resize_output_folder"] = e.path
                resize_output_text.value = f"Carpeta de salida: {e.path}"
                if resize_output_text.page:  # Verificar que el control está asociado a la página
                    resize_output_text.update()
                else:
                    print("Error: resize_output_text no está asociado a la página.")
            else:
                state["resize_input_folder"] = e.path
                resize_input_text.value = f"Carpeta de entrada: {e.path}"
                if resize_input_text.page:  # Verificar que el control está asociado a la página
                    resize_input_text.update()
                else:
                    print("Error: resize_input_text no está asociado a la página.")

        # Vista de eliminar fondo
        elif state["current_view"] == "delete_background":
            if state["selecting_destination"]:
                state["output_folder"] = e.path
                carpeta_destino_text.value = f"Carpeta de destino: {e.path}"
                carpeta_destino_text.update()
            else:
                state["input_folder"] = e.path
                carpeta_origen_text.value = f"Carpeta de origen: {e.path}"
                carpeta_origen_text.update()
        
        elif state["current_view"] == "rename":
            state["rename_folder"] = e.path
            carpeta_text.value = f"Carpeta seleccionada: {e.path}"
            if carpeta_text.page:  # Verificar que el control está en la página
                carpeta_text.update()
        
        # Asegúrate de reflejar los cambios en la página
        page.update()
