import flet as ft
from deletes import delete_all_duplicates

 # Variables de estado
state = {
        "current_duplicates": [],
        "current_view": "duplicates"
    }
    
selected_dir_text = ft.Text(
        value="No se ha seleccionado ninguna carpeta",
        size=14,
        color=ft.colors.BLUE_200
    )
    
result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)
    
duplicates_list = ft.ListView(
        expand=1,
        spacing=10,
        height=200,
    )
    
delete_all_button = ft.ElevatedButton(
        "Eliminar TODOS los duplicados",
        color=ft.colors.WHITE,
        bgcolor=ft.colors.RED_800,
        icon=ft.icons.DELETE_SWEEP,
        visible=False,
        on_click=lambda e: delete_all_duplicates()
    )
    
 # Controles para la vista de organizar archivos
organize_dir_text = ft.Text(
        "No se ha seleccionado ninguna carpeta",
        size=14,
        color=ft.colors.BLUE_200,
    )


organize_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)