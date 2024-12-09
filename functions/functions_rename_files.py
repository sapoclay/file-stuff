import flet as ft
from functionalities.rename_all_files import bulk_rename_files

def seleccionar_carpeta(folder_picker):
    """
    Abre el selector de carpetas.
    """
    folder_picker.get_directory_path()

def renombrar_archivos(state, name_template_field, snack_bar, page):
    """
    Renombra archivos en una carpeta seleccionada utilizando una plantilla de nombres.
    """
    if not state.get("rename_folder"):
        snack_bar.content.value = "Selecciona una carpeta primero."
        snack_bar.open = True
        page.update()
        return

    if not name_template_field.value:
        snack_bar.content.value = "Especifica una plantilla de nombre."
        snack_bar.open = True
        page.update()
        return

    if '###' not in name_template_field.value:
        snack_bar.content.value = "Error: La plantilla debe contener '###' para indicar la posición del contador."
        snack_bar.open = True
        page.update()
        return

    # Llamar a la función para renombrar archivos
    result = bulk_rename_files(state["rename_folder"], name_template_field.value, snack_bar)
    if isinstance(result, list):
        snack_bar.content.value = f"Archivos renombrados correctamente. Total: {len(result)}"
    else:
        snack_bar.content.value = f"Error: {result}"
    snack_bar.open = True
    page.update()
