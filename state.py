import flet as ft
from deletes import delete_all_duplicates

 # Variables de estado
state = {
        "current_duplicates": [],
        "current_view": "duplicates",
        "resize_input_folder": "",
        "resize_output_folder": "",
        "selecting_resize_output": False,
    }
    
selected_dir_text = ft.Text(
        value="No se ha seleccionado ninguna carpeta",
        size=14,
        color=ft.colors.BLUE_200
    )

selected_bulk_text = ft.Text(
    value="No se ha seleccionado ninguna carpeta",
    size = 14,
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

# Controles para la vista de redimensionar imágenes
resize_input_text = ft.Text(
    "Carpeta de entrada: No seleccionada",
    size=14,
    color=ft.colors.BLUE_200,
)

resize_output_text = ft.Text(
    "Carpeta de salida: No seleccionada",
    size=14,
    color=ft.colors.BLUE_200,
)

resize_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)


