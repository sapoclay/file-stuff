import flet as ft
from functionalities.organize_files import organize_folder

def organize_directory(directory, organize_result_text):
    try:
        organize_folder(directory)
        organize_result_text.value = "Archivos organizados correctamente!!!"
        organize_result_text.color = ft.Colors.GREEN_500
    except Exception as e:
        organize_result_text.value = f"Error al organizar archivos: {str(e)}"
        organize_result_text.color = ft.Colors.RED_500
    organize_result_text.update()
