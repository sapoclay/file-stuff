import flet as ft

# Variables de estado
state = {
    "current_duplicates": [],
    "current_view": "duplicates",
    "resize_input_folder": "",
    "resize_output_folder": "",
    "selecting_resize_output": False,
    "convert_input_file": "",
}

# Controles de la interfaz
selected_dir_text = ft.Text(
    "No se ha seleccionado ninguna carpeta",
    size=14,
    color=ft.Colors.BLUE_100
)

result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)

duplicates_list = ft.ListView(
    expand=1,  # TRUE
    spacing=10,
    height=200,
)

# Botón para eliminar todos los archivos duplicados
delete_all_button = ft.ElevatedButton(
    "Eliminar Todos los Archivos Duplicados",
    color=ft.Colors.WHITE,
    bgcolor=ft.Colors.RED_900,
    icon=ft.Icons.DELETE_SWEEP,
    visible=False,
    on_click=lambda e: delete_all_duplicates()  # Define esta función más adelante
)

# Controles para la vista de organizar archivos
organize_dir_text = ft.Text(
    "No se ha seleccionado ninguna carpeta",
    size=14,
    color=ft.Colors.BLUE_200
)

organize_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)

# Controles para la vista de redimensionar imágenes
resize_input_text = ft.Text(
    "Carpeta de entrada: No seleccionada",
    size=14,
    color=ft.Colors.BLUE_200
)

resize_output_text = ft.Text(
    "Carpeta de salida: No seleccionada",
    size=14,
    color=ft.Colors.BLUE_200
)

resize_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)

width_field = ft.TextField(
    label="Ancho",
    value="800",
    width=100,
    text_align=ft.TextAlign.RIGHT,
    keyboard_type=ft.KeyboardType.NUMBER,
)

height_field = ft.TextField(
    label="Alto",
    value="600",
    width=100,
    text_align=ft.TextAlign.RIGHT,
    keyboard_type=ft.KeyboardType.NUMBER,
)

# Controles para la vista de convertir imágenes
convert_input_text = ft.Text(
    "No se ha seleccionado ninguna imagen",
    size=14,
    color=ft.Colors.BLUE_200
)

convert_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)

format_dropdown = ft.Dropdown(
    label="Formato de Salida",
    width=200,
    options=[
        ft.dropdown.Option("PNG"),
        ft.dropdown.Option("JPEG"),
        ft.dropdown.Option("WEBP"),
        ft.dropdown.Option("BMP"),
        ft.dropdown.Option("GIF"),
    ],
    value="PNG"
)