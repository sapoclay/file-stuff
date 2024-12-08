import flet as ft
from functionalities.delete_duplicates import find_duplicates, delete_file

def scan_directory(directory, state, result_text, delete_all_button, duplicates_list):
    try:
        # Limpiar la lista de duplicados
        duplicates_list.controls.clear()
        state["current_duplicates"] = find_duplicates(directory)

        if not state["current_duplicates"]:
            result_text.value = "No se han encontrado archivos duplicados"
            result_text.color = ft.Colors.GREEN_500
            delete_all_button.visible = False
        else:
            result_text.value = f"Se encontraron {len(state['current_duplicates'])} archivos duplicados"
            result_text.color = ft.Colors.ORANGE_500
            delete_all_button.visible = True

            # Generar controles para cada duplicado
            for dup_file, original in state["current_duplicates"]:
                dup_row = ft.Row([
                    ft.Text(
                        f"Duplicado: {dup_file}\nOriginal: {original}",
                        size=12,
                        expand=True,
                        color=ft.Colors.BLUE_200,
                    ),
                    ft.ElevatedButton(
                        "Eliminar",
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.RED_900,
                        on_click=lambda e, path=dup_file: delete_duplicate(
                            path, state, result_text, duplicates_list, delete_all_button
                        ),
                    ),
                ])
                duplicates_list.controls.append(dup_row)

        # Validar y actualizar los controles
        if duplicates_list.page:  # Verificar que duplicates_list está asociado a la página
            duplicates_list.update()
        else:
            print("Error: duplicates_list no está asociado a la página.")

        if result_text.page:  # Verificar que result_text está asociado a la página
            result_text.update()
        else:
            print("Error: result_text no está asociado a la página.")

        if delete_all_button.page:  # Verificar que delete_all_button está asociado a la página
            delete_all_button.update()
        else:
            print("Error: delete_all_button no está asociado a la página.")

    except Exception as e:
        # Manejar errores al escanear el directorio
        result_text.value = f"Error al escanear el directorio: {str(e)}"
        result_text.color = ft.Colors.RED_500
        if result_text.page:  # Actualizar solo si está asociado
            result_text.update()


def delete_duplicate(filepath, state, result_text, duplicates_list, delete_all_button):
    try:
        if delete_file(filepath):
            result_text.value = f"Archivo eliminado: {filepath}"
            result_text.color = ft.Colors.GREEN_500
            # Actualizar lista de duplicados
            for control in duplicates_list.controls[:]:
                if filepath in control.controls[0].value:
                    duplicates_list.controls.remove(control)
            # Actualizar el estado de duplicados
            state["current_duplicates"] = [
                (dup, orig) for dup, orig in state["current_duplicates"] if dup != filepath
            ]
            # Ocultar el botón si ya no hay duplicados
            if not state["current_duplicates"]:
                delete_all_button.visible = False
        else:
            result_text.value = f"Error al eliminar: {filepath}"
            result_text.color = ft.Colors.RED_500
    except Exception as e:
        result_text.value = f"Error inesperado al eliminar: {str(e)}"
        result_text.color = ft.Colors.RED_500

    duplicates_list.update()
    result_text.update()
    delete_all_button.update()

def delete_all_duplicates(state, result_text, duplicates_list, delete_all_button):
    """Elimina todos los archivos duplicados."""
    deleted_count = 0
    failed_count = 0
    
    for dup_file, _ in state["current_duplicates"][:]:
        if delete_file(dup_file):
            deleted_count += 1
        else:
            failed_count += 1
    duplicates_list.controls.clear()
    state["current_duplicates"] = []
    delete_all_button.visible = False
    
    if failed_count == 0:
        result_text.value = f"Se eliminaron exitosamente {deleted_count} archivos duplicados"
        result_text.color = ft.Colors.GREEN_500
    else:
        result_text.value = f"Se eliminaron {deleted_count} archivos. Fallaron {failed_count} archivos."
        result_text.color = ft.Colors.RED_500
    
    duplicates_list.update()
    result_text.update()
    delete_all_button.update()
