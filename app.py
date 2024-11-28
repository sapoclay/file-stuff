import flet as ft
from functionalities.delete_duplicates import find_duplicates, delete_file
from functionalities.organize_files import organize_folder
from functionalities.resize_files import batch_resize
from functionalities.converter_images import convert_img

def main(page: ft.Page):
    
    # Configuración de la ventana principal
    page.title = "File Stuff"
    page.window.width = 800
    page.window.height = 600
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_800
    page.theme_mode = ft.ThemeMode.DARK
    
    # Tema personalizado
    page.theme = ft.Theme(
        color_scheme_seed = ft.Colors.PURPLE,
        visual_density = ft.VisualDensity.COMFORTABLE,
        color_scheme = ft.ColorScheme(
            primary = ft.Colors.BLUE,
            secondary = ft.Colors.RED,
            background = ft.Colors.GREY_900,
            surface = ft.Colors.GREY_800,
        )
    )
    
    # VARIABLES DE ESTADO
    state = {
        "current_duplicates": [],
        "current_view": "duplicates",
        "resize_input_folder": "",
        "resize_output_folder": "",
        "selecting_resize_output": False,
        "convert_input_file": "",
    }
    selected_dir_text = ft.Text(
        "No se ha seleccionado ninguna carpeta",
        size = 14,
        color = ft.Colors.BLUE_100
    )
    
    result_text = ft.Text(size = 14, weight = ft.FontWeight.BOLD)
    
    duplicates_list = ft.ListView(
        expand = 1, # TRUE
        spacing = 10,
        height = 200,
    )
    
    # Variable de estado, Botón eliminar todos los archivos duplicados
    delete_all_button = ft.ElevatedButton(
        "Eliminar Todos los Archivos Duplicados",
        color = ft.Colors.WHITE,
        bgcolor = ft.Colors.RED_900,
        icon = ft.Icons.DELETE_SWEEP,
        visible = False,
        on_click = lambda e: delete_all_duplicates()
    )    
    
    # Controles para la vista de organizar archivos
    organize_dir_text = ft.Text(
        "No se ha seleccionado ninguna carpeta",
        size = 14,
        color = ft.Colors.BLUE_200
    )
    
    organize_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)
    
    # Controles para la vista de redimensionar imágenes
    resize_input_text = ft.Text(
        "Carpeta de entrada: No seleccionada",
        size = 14,
        color = ft.Colors.BLUE_200
    )
    
    resize_output_text = ft.Text(
        "Carpeta de salida: No seleccionada",
        size = 14,
        color = ft.Colors.BLUE_200
    )
    
    resize_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)
    
    width_field = ft.TextField (
        label = "Ancho",
        value = "800",
        width = 100,
        text_align = ft.TextAlign.RIGHT,
        keyboard_type = ft.KeyboardType.NUMBER,
    )
    
    height_field = ft.TextField (
        label = "Alto",
        value = "600",
        width = 100,
        text_align = ft.TextAlign.RIGHT,
        keyboard_type = ft.KeyboardType.NUMBER,
    )
    
    # Controles para la vista de convertir imágenes
    
    convert_input_text = ft.Text(
        "No se ha seleccionado ninguna imagen",
        size = 14,
        color = ft.Colors.BLUE_200
    )
    
    convert_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)
    
    format_dropdown = ft.Dropdown(
        label = "Formato de Salida",
        width = 200,
        options = [
            ft.dropdown.Option("PNG"),
            ft.dropdown.Option("JPEG"),
            ft.dropdown.Option("WEBP"),
            ft.dropdown.Option("BMP"),    
            ft.dropdown.Option("GIF"),
        ],
        value = "PNG"
    )
    
    # MENÚ LATERAL CAMBIO VISTAS
    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            state["current_view"] = "duplicates"
            content_area.content = duplicate_files_view
        elif selected == 1:
            state["current_view"] = "organize"
            content_area.content = organize_files_view
        elif selected == 2:
            state["current_view"] = "resize"
            content_area.content = resize_files_view
        elif selected == 3:
            state["current_view"] = "convert"
            content_area.content = convert_images_view
        elif selected == 4:
            state["current_view"] = "about"
            content_area.content = about_view
        content_area.update()
        
    def handle_file_picker(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0: # un archivo, mayor que 0
            file_path = e.files[0].path
            state["convert_input_file"] = file_path
            convert_input_text.value = f"Imagen seleccionada: {file_path}"
            convert_input_text.update()
    
    def handle_folder_picker(e: ft.FilePickerResultEvent):
        if e.path:
            if state["current_view"] == "duplicates":
                selected_dir_text.value = f"Carpeta seleccionada: {e.path}"
                selected_dir_text.update()
                scan_directory(e.path)
            elif state["current_view"] == "organize":
                organize_dir_text.value = f"Carpeta seleccionada: {e.path}"
                organize_dir_text.update()
                organize_directory(e.path)
            elif state["current_view"] == "resize":
                if state["selecting_resize_output"]:
                    state["resize_output_folder"] = e.path
                    resize_output_text.value = f"Carpeta de salida: {e.path}"
                    resize_output_text.update()
                else:
                    state["resize_input_folder"] = e.path
                    resize_input_text.value = f"Carpeta de entrada: {e.path}"
                    resize_input_text.update()
                
    def select_input_folder():
        state["selecting_resize_output"] = False
        folder_picker.get_directory_path()
        
    def select_output_folder():
        state["selecting_resize_output"] = True
        folder_picker.get_directory_path()
        
    def convert_image():
        try:
            if not state["convert_input_file"]:
                convert_result_text.value = "ERROR!! Selecciona una imagen"
                convert_result_text.color = ft.colors.RED_500
                convert_result_text.update()
                return
            if not format_dropdown.value:
                convert_result_text.value = "ERROR!! Selecciona un formato de salida válido"
                convert_result_text.color = ft.colors.RED_500
                convert_result_text.update()
                return
            convert_img(state["convert_input_file"], format_dropdown.value)
            convert_result_text.value = "Imagen convertida exitosamente!!!"
            convert_result_text.color = ft.colors.GREEN_500
            convert_result_text.update()
        except Exception as e:
            convert_result_text.value = f"ERROR al convertir la imagen: {str(e)}"
            convert_result_text.color = ft.colors.RED_500
            convert_result_text.update()
        
    def resize_images():
        try:
            if not state["resize_input_folder"] or not state["resize_output_folder"]:
                resize_result_text.value = "Error!! Selecciona las carpetas de ENTRADA y de SALIDA"
                resize_result_text.color = ft.colors.RED_500
                resize_result_text.update()
                return
            # Pasamos los valores a enteros
            width = int(width_field.value)
            height = int(height_field.value)
            
            # Comprobamos si los valores son menores o iguales a 0
            if width <= 0 or height <= 0:
                resize_result_text.value = "Error!! Las dimensiones deben ser mayores que 0"
                resize_result_text.color = ft.colors.RED_500
                resize_result_text.update()
                return

            batch_resize(state["resize_input_folder"], state["resize_output_folder"], width, height)
            resize_result_text.value = "Imágenes redimensionadas correctamente!!"
            resize_result_text.color = ft.colors.GREEN_500
            resize_result_text.update()
        except ValueError:
            resize_result_text.value = "Error!! Ingresa dimensiones válidas. SOLO NÚMEROS MAYORES QUE 0."
            resize_result_text.color = ft.colors.RED_500
            resize_result_text.update()
        except Exception as e:
            resize_result_text.value = f"Error al redimensionar: {str(e)}"
            resize_result_text.color = ft.colors.RED_500
            resize_result_text.update()
                
    # Función para organizar los archivos
    def organize_directory(directory):
        try:
            organize_folder(directory)
            organize_result_text.value = "Archivos organizados correctamente!!!"
            organize_result_text.color = ft.colors.GREEN_500
        except Exception as e:
            organize_result_text.value = f"Error al organizar archivos: {str(e)}"
            organize_result_text.color = ft.colors.RED_500
        organize_result_text.update()
                
    # Escaneado de directorio buscando archivos duplicados
    def scan_directory(directory):
        duplicates_list.controls.clear()
        state["current_duplicates"] = find_duplicates(directory)
        
        if not state["current_duplicates"]:
            result_text.value = "No se han encontrado archivos duplicados"
            result_text.color = ft.colors.GREEN_500
            delete_all_button.visible = False
        else:
            result_text.value = f"Se encontraron {len(state["current_duplicates"])} archivos duplicados"
            result_text.color = ft.colors.ORANGE_500
            delete_all_button.visible = True
            
            for dup_file, original in state["current_duplicates"]:
                dup_row = ft.Row([
                    ft.Text(
                        f"Duplicado {dup_file}\nOriginal: {original}",
                        size = 12,
                        expand = True,
                        color = ft.colors.BLUE_200
                    ),
                    ft.ElevatedButton(
                        "Eliminar",
                        color = ft.colors.WHITE,
                        bgcolor = ft.colors.RED_900,
                        on_click = lambda e, path = dup_file: delete_duplicate(path)
                    )
                ])
                duplicates_list.controls.append(dup_row)
        duplicates_list.update()
        result_text.update()
        delete_all_button.update()
    
    # Función para eliminar UN SOLO archivo duplicado
    def delete_duplicate(filepath):
        if delete_file(filepath):
            result_text.value = f"Archivo eliminado: {filepath}"
            result_text.color = ft.colors.GREEN_500
            for control in duplicates_list.controls[:]:
                if filepath in control.controls[0].value:
                    duplicates_list.controls.remove(control)
            state["current_duplicates"] = [(dup, orig) for dup, orig in state["current_duplicates"] if dup != filepath]
            if not state["current_duplicates"]:
                delete_all_button.visible = False
        else:
            result_text.value = f"Error al eliminar: {filepath}"
            result_text.color = ft.colors.RED_500
        
        duplicates_list.update()
        result_text.update()
        delete_all_button.update()
            
        
    # Función para eliminar todos los archivo duplicados
    def delete_all_duplicates():
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
            result_text.color = ft.colors.GREEN_500
        else:
            result_text.value = f"Se eliminaron {deleted_count} archivos. Fallaron {failed_count} archivos."
            result_text.color = ft.colors.RED_500
        
        duplicates_list.update()
        result_text.update()
        delete_all_button.update()
        
    def abrir_repositorio(_):
        # Solo abrimos la URL sin parámetros adicionales
        page.launch_url("https://github.com/sapoclay/file-stuff")

    
    # Configurar los selectores de ARCHIVOS para el convertor
    file_picker = ft.FilePicker(
        on_result = handle_file_picker
    )
    
    file_picker.file_type = ft.FilePickerFileType.IMAGE # permite seleccionar solo Imágenes
    file_picker.allowed_extensions = ["png", "jpg", "jpeg", "gif", "bmp", "webp"] # extensiones permitidas
    
    # Configurar el selector de CARPETAS
    folder_picker  = ft.FilePicker(on_result = handle_folder_picker)
    page.overlay.extend([folder_picker, file_picker])
    
    # Vista de archivos duplicados
    duplicate_files_view = ft.Container(
        content = ft.Column([
            ft.Container(
                content = ft.Text(
                    "Eliminar Archivos Duplicados",
                    size = 28,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.BLUE_200
                ),
                margin = ft.margin.only(bottom=20)
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Seleccionar Carpeta",
                    icon = ft.Icons.FOLDER_OPEN,
                    color = ft.Colors.WHITE,
                    bgcolor = ft.Colors.BLUE_900,
                    on_click = lambda _: folder_picker.get_directory_path()
                ),
                delete_all_button,
            ]),
            ft.Container(
                content = selected_dir_text, # variable de estado que se actualiza 
                margin = ft.margin.only(top = 10, bottom = 10)
            ),
            result_text,
            ft.Container(
                content = duplicates_list,
                border = ft.border.all(2, ft.Colors.BLUE_500),
                border_radius = 10,
                padding = 20,
                margin = ft.margin.only(top=10),
                bgcolor = ft.Colors.GREY_800,
                expand = True                
            )
        ]),
        padding = 30,
        expand = True        
    )
    
    # Vista de organizar archivos
    organize_files_view = ft.Container(
        content = ft.Column([
            ft.Container(
                content = ft.Text(
                    "Organizar archivos por TIPO",
                    size = 28,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.BLUE_200
                ),
                margin = ft.margin.only(bottom=20)
            ),
            ft.ElevatedButton(
                "Seleccionar Carpeta",
                icon = ft.Icons.FOLDER_OPEN,
                color = ft.Colors.WHITE,
                bgcolor = ft.Colors.BLUE_900,
                on_click = lambda _: folder_picker.get_directory_path()
            ),
            ft.Container(
                content = organize_dir_text,
                margin = ft.margin.only(top=10, bottom=10)
            ),
            organize_result_text,
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Los archivos serán organizador en las siguientes carpetas:",
                        size = 14,
                        color = ft.Colors.BLUE_200
                    ),
                    ft.Text("- Imágenes (.jpeg, .jpg, .png, .gif, .webp)", size = 14),
                    ft.Text("- Vídeos (.mp4, .mkv, .avi, .mov)", size = 14),
                    ft.Text("- Documentos (.pdf, .docx, .txt, .m3u8, .m3u)", size = 14),
                    ft.Text("- Datasets (.xlsx, .csv, .png, .gif, .webp)", size = 14),
                    ft.Text("- Comprimidos (.zip, .rar, .gv)", size = 14),
                    ft.Text("- Programas (.deb, .appImage, .exe, .msi, .snap, .flatpak)", size = 14),
                ]),
                border = ft.border.all(2, ft.Colors.BLUE_500),
                border_radius = 10,
                padding = 20,
                margin = ft.margin.only(top=10),
                bgcolor = ft.Colors.GREY_800,
            )
        ]),
        padding = 30,
        expand = True
    )
    
    # Vista para redimensionar imagenes
    resize_files_view = ft.Container(
        content = ft.Column([
            ft.Container(
                content=ft.Text(
                    "Redimensaionar Imágenes",
                    size = 28,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.BLUE_200
                ),
                margin = ft.margin.only(bottom=20)
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Seleccionar Carpeta de Entrada",
                    icon = ft.Icons.FOLDER_OPEN,
                    color = ft.Colors.WHITE,
                    bgcolor = ft.Colors.BLUE_900,
                    on_click = lambda _: select_input_folder()
                ),
                ft.ElevatedButton(
                    "Seleccionar Carpeta de Salida",
                    icon = ft.Icons.FOLDER_OPEN,
                    color = ft.Colors.WHITE,
                    bgcolor = ft.Colors.BLUE_900,
                    on_click = lambda _: select_output_folder()
                ),
            ]),
            ft.Container(
                content = ft.Column([
                    resize_input_text,
                    resize_output_text
                ]),
                margin = ft.margin.only(top=10, bottom=10)
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Dimensiones de la imagen:",
                        size = 14,
                        color = ft.Colors.BLUE_200
                    ),
                    ft.Row([
                        width_field,
                        ft.Text("x", size = 20),
                        height_field,
                        ft.Text(" píxeles", size = 14)
                    ]),
                ]),
                margin = ft.margin.only(bottom=10)
            ),
            ft.ElevatedButton(
                "Redimensionar Imágenes",
                icon = ft.Icons.PHOTO_SIZE_SELECT_LARGE,
                color = ft.Colors.WHITE,
                bgcolor = ft.Colors.BLUE_900,
                on_click = lambda _: resize_images()
            ),
            resize_result_text,
            ft.Container(
                content = ft.Column([
                    ft.Text(
                        "Información:",
                        size = 14,
                        color = ft.Colors.BLUE_500
                    ),
                    ft.Text("- Se procesarán archivos .jpg, .jpeg, .png, .gif y .webp", size=14),
                    ft.Text("- Las imágenes originales no serán modificadas", size=14),
                    ft.Text("- Las imágenes redimensionadas se guardarán con el prefijo 'resized_'", size=14)
                ]),
                border = ft.border.all(2, ft.Colors.BLUE_500),
                border_radius = 10,
                padding = 20,
                margin = ft.margin.only(top=10),
                bgcolor = ft.Colors.GREY_800,
            )
        ]),
        padding = 30,
        expand = True
    )
    
    # Vista para convertir imágenes
    convert_images_view = ft.Container(
        content = ft.Column([
            ft.Container(
                content = ft.Text(
                    "Convertir Formato de Imagen",
                    size = 28,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.BLUE_200
                ),
                margin = ft.margin.only(bottom=20)
            ),
            ft.ElevatedButton(
                "Seleccionar Imagen",
                icon = ft.Icons.IMAGE,
                color = ft.Colors.WHITE,
                bgcolor = ft.Colors.BLUE_900,
                on_click = lambda _: file_picker.pick_files()
            ),
            ft.Container(
                content = convert_input_text,
                margin = ft.margin.only(top=10, bottom=10)
            ),
            format_dropdown,
            ft.Container(
                margin = ft.margin.only(top=10),
                content = ft.ElevatedButton(
                    "Convertir Imagen",
                    icon = ft.Icons.TRANSFORM,
                    color = ft.Colors.WHITE,
                    bgcolor=ft.Colors.BLUE_900,
                    on_click = lambda _: convert_image()
                ),
            ),
            convert_result_text,
            ft.Container(
                content = ft.Column([
                    ft.Text(
                        "Información:",
                        size = 14,
                        color = ft.Colors.BLUE_200
                    ),
                    ft.Text("- Formatos soportados: PNG, JPEG, WEBP, BMP, GIF", size=14),
                    ft.Text("- La imagen original no será modificada", size=14),
                    ft.Text("- La imagen convertida se guardará en la misma carpeta que la orginal", size=14),
                    ft.Text("- Al convertir a JPEG, las imágenes con transparencia se convertirán a fondo blanco", size=14),
                ]),
                border = ft.border.all(2, ft.Colors.BLUE_500),
                border_radius = 10,
                padding = 20,
                margin = ft.margin.only(top=10),
                bgcolor = ft.Colors.GREY_800,
            )
        ]),
        padding = 30,
        expand = True
    )
    
   # Vista de información
    about_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text(
                    "Acerca de File Stuff",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200  
                ),
                margin=ft.margin.only(bottom=20)
            ),
            ft.Image(
                src="./assets/logo.png",
                width=200,
                height=200,
                fit=ft.ImageFit.CONTAIN,  
            ),
            ft.Text(
                "File Stuff es una aplicación básica para gestionar archivos.",
                size=16,
                color=ft.Colors.BLUE_500,  
            ),
            ft.ElevatedButton(
                "Visitar repositorio",
                icon=ft.Icons.LINK,  
                color=ft.Colors.WHITE,  
                bgcolor=ft.Colors.BLUE_900,
                on_click=abrir_repositorio,  
            ),
            ft.Text(
                "entreunosyceros.net",
                size=14,
                color=ft.Colors.GREY_600,  
            ),
        ]),
        padding=30,
        expand=True
    )
    
    # Vista por defecto de la aplicación ... la 0.
    content_area = ft.Container(
        content = duplicate_files_view,
        expand = True,
    )
    
    # Extructura menú lateral
    rail=ft.NavigationRail(
        selected_index = 0,
        label_type = ft.NavigationRailLabelType.ALL,
        min_width = 100,
        min_extended_width = 200,
        group_alignment = -1,
        destinations = [
            ft.NavigationRailDestination(
                icon = ft.Icons.DELETE_FOREVER,
                selected_icon = ft.Icons.DELETE_FOREVER,
                label = "Duplicados",
            ),
            ft. NavigationRailDestination(
                icon = ft.Icons.FOLDER_COPY,
                selected_icon = ft.Icons.FOLDER_COPY,
                label = "Organizar",    
            ),
            ft. NavigationRailDestination(
                icon = ft.Icons.PHOTO_SIZE_SELECT_LARGE,
                selected_icon = ft.Icons.PHOTO_SIZE_SELECT_LARGE,
                label = "Redimensionar",    
            ),
            ft. NavigationRailDestination(
                icon = ft.Icons.TRANSFORM,
                selected_icon = ft.Icons.TRANSFORM,
                label = "Convertir",    
            ),
            ft.NavigationRailDestination(
                icon = ft.Icons.INFO,
                selected_icon = ft.Icons.INFO,
                label = "About",
            ),
        ],
        on_change = change_view,
        bgcolor = ft.Colors.GREY_900,
    )
    
    page.add(
        ft.Row(
            [
                    rail,
                    ft.VerticalDivider(width = 1),
                    content_area,
            ],
            expand = True,
        )
    )
    

if __name__ == "__main__":
    ft.app(target=main)