import flet as ft
from borrar_archivos_duplicados import delete_file

# Función para eliminar duplicados uno a uno
CURRENT_DUPLICATES = "current_duplicates"
def delete_duplicate(filepath):
    from state import state,  delete_all_button,  result_text, duplicates_list

    if delete_file(filepath):
        result_text.value = f"Archivo eliminado: {filepath}"
        result_text.color = ft.colors.GREEN_400
        for control in duplicates_list.controls[:]:
            if filepath in control.controls[0].value:
                duplicates_list.controls.remove(control)
        state[CURRENT_DUPLICATES] = [
            (dup, orig) for dup, orig in state[CURRENT_DUPLICATES] if dup != filepath
        ]
        if not state[CURRENT_DUPLICATES]:
            delete_all_button.visible = False
    else:
        result_text.value = f"Error al eliminar: {filepath}"
        result_text.color = ft.colors.RED_400

    duplicates_list.update()
    result_text.update()
    delete_all_button.update()


    # Función para eliminar TODOS los duplicados
def delete_all_duplicates():
    from state import state,  delete_all_button,  result_text, duplicates_list

    delete_count = 0
    failed_count = 0
    for dup_file, _ in state[CURRENT_DUPLICATES][:]:
        if delete_file(dup_file):
            delete_count += 1
        else:
            failed_count += 1

    duplicates_list.controls.clear()
    state[CURRENT_DUPLICATES] = []
    delete_all_button.visible = False

    if failed_count == 0:
        result_text.value = f"Se eliminaron exitosamente {delete_count} archivos duplicados"
        result_text.color = ft.colors.GREEN_400
    else:
        result_text.value = f"Se eliminaron {delete_count} archivos. Fallaron {failed_count} archivos al ser eliminados"
        result_text.color = ft.colors.RED_400

    duplicates_list.update()
    result_text.update()
    delete_all_button.update()