import flet as ft
from functions.functions_duplicate_files import delete_all_duplicates

# Variables de estado
state = {
    "current_duplicates": [],
    "current_view": "duplicates",
    "resize_input_folder": "",
    "resize_output_folder": "",
    "selecting_resize_output": False,
    "convert_input_file": "",
    "rename_folder": None,
    "current_view": "pdf_converter",  # Establecer la vista por defecto en pdf_converter
    "pdf_file_path": "",  # Almacena la ruta del archivo PDF seleccionado
    "selected_dir": None,  # Variable para guardar la carpeta seleccionada para fusionar pdfs

    
}

# Controles compartidos entre las vistas
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

delete_all_button = ft.ElevatedButton(
    "Eliminar Todos los Archivos Duplicados",
    color=ft.Colors.WHITE,
    bgcolor=ft.Colors.RED_900,
    icon=ft.Icons.DELETE_SWEEP,
    visible=False,
    on_click=lambda e: delete_all_duplicates(state, result_text, duplicates_list, delete_all_button),
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
    value="PNG",
)

# Controles para la vista eliminar fondo

carpeta_origen_text = ft.Text(
    "Carpeta de origen: No seleccionada",
    size=14,
    color=ft.Colors.BLUE_200,
)

carpeta_destino_text = ft.Text(
    "Carpeta de destino: No seleccionada",
    size=14,
    color=ft.Colors.BLUE_200,
)

# Controles para la vista rename_all_Files

carpeta_text = ft.Text(
    "Carpeta seleccionada: No seleccionada",
    size=14,
    color=ft.Colors.BLUE_200,
)

# Dropdown para seleccionar el formato de salida para convertir PDF
output_format_dropdown = ft.Dropdown(
    label="Selecciona el formato de salida",
    options=[
        ft.dropdown.Option("docx", "DOCX"),
        ft.dropdown.Option("odt", "ODT"),
    ],
    value="docx",
)

pdf_file_text = ft.Text(
    "Archivo seleccionado: No seleccionado",
    size=14,
    color=ft.Colors.BLUE_200,
)

# Mensajes de error o éxito (estos se pueden usar en el Snackbar)
snack_bar = ft.SnackBar(
    content=ft.Text(""),
    duration=2000,  # Duración del mensaje en milisegundos
)

# Mensaje de error o éxito para la vista de fusionar PDFs
pdf_dir = ft.Text(
    "Carpeta de salida: No seleccionada",
    size=14,
    color=ft.Colors.BLUE_200,
)