import flet as ft
from theme import configurar_ventana, configurar_tema

from functions.functions_duplicate_files import scan_directory
from functions.functions_organize_files import organize_directory  

from functions.functions_folder_picker import handle_folder_picker 
from functions.functions_convert_images import convert_image_function

from views.about_view import view_about
from views.duplicate_files_view import duplicate_files_view
from views.organize_files_view import organize_files_view  
from views.resize_files_view import resize_files_view  
from views.convert_files_view import convert_images_view
from views.delete_background_view import delete_background_view
from views.rename_files_view import rename_files_view


# Importar variables de estado y controles
from state_controls import (
    state,
    selected_dir_text,
    result_text,
    duplicates_list,
    delete_all_button,
    organize_dir_text,
    organize_result_text,
    resize_input_text,
    resize_output_text,
    resize_result_text,
    carpeta_origen_text,  
    carpeta_destino_text,  
    carpeta_text,
    width_field,
    height_field,
    convert_input_text,
    convert_result_text,
    format_dropdown,
)

def main(page: ft.Page):
    # Configurar la ventana principal
    configurar_ventana(page)
    
    # Aplicar el tema personalizado
    page.theme = configurar_tema()
    
    # Definir snack_bar
    snack_bar = ft.SnackBar(
        content=ft.Text(""),
        duration=2000,  # Duración del mensaje en milisegundos
    )
    page.overlay.append(snack_bar)
        
    # MENÚ LATERAL CAMBIO VISTAS
    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            state["current_view"] = "duplicates"
            content_area.content = duplicate_files_view(
                page, state, folder_picker, result_text, delete_all_button, selected_dir_text, duplicates_list
            )
        elif selected == 1:
            state["current_view"] = "organize"
            content_area.content = organize_files_view(
                page, state, folder_picker, organize_dir_text, organize_result_text
            )
        elif selected == 2:
            state["current_view"] = "resize"
            content_area.content = resize_files_view(
            page,
            state,
            folder_picker,
            resize_input_text,
            resize_output_text,
            resize_result_text,
            width_field,
            height_field
        )
        elif selected == 3:
            state["current_view"] = "convert"
            content_area.content = convert_images_view(
            page,
            state,
            file_picker,
            convert_input_text,
            format_dropdown,
            convert_result_text,
            convert_image_function,
        )
        elif selected == 4:  # Índice para la nueva vista
            state["current_view"] = "delete_background"
            content_area.content = delete_background_view(
                page, state, folder_picker, snack_bar, carpeta_origen_text, carpeta_destino_text
            )
        elif selected == 5:  # Índice para la nueva vista
            state["current_view"] = "rename"
            content_area.content = rename_files_view(
                page, state, folder_picker, snack_bar, carpeta_text
            )
        elif selected == 6:
            state["current_view"] = "about"
            content_area.content = view_about(page)
        content_area.update()
        
    def handle_file_picker(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0: # un archivo, mayor que 0
            file_path = e.files[0].path
            state["convert_input_file"] = file_path
            convert_input_text.value = f"Imagen seleccionada: {file_path}"
            convert_input_text.update()           
       
    # Configurar los selectores de ARCHIVOS para el convertor
    file_picker = ft.FilePicker(
        on_result = handle_file_picker
    )
    
    file_picker.file_type = ft.FilePickerFileType.IMAGE # permite seleccionar solo Imágenes
    file_picker.allowed_extensions = ["png", "jpg", "jpeg", "gif", "bmp", "webp"] # extensiones permitidas
    
    # Configurar el selector de CARPETAS
    folder_picker = ft.FilePicker(
        on_result=lambda e: handle_folder_picker(
            e,  # Este es el evento, ya está siendo pasado automáticamente
            state,
            page,
            selected_dir_text,
            scan_directory,
            organize_directory,
            resize_input_text,
            resize_output_text,
            folder_picker,
            result_text,
            delete_all_button,
            duplicates_list,
            organize_result_text,
            carpeta_origen_text, 
            carpeta_destino_text,
            organize_dir_text,
            carpeta_text
        )
    )
    page.overlay.extend([folder_picker, file_picker])
        
    # Vista por defecto de la aplicación ... la 0.
    content_area = ft.Container(
        content=duplicate_files_view(page, state, folder_picker, result_text, delete_all_button, selected_dir_text, duplicates_list),
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
                icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                selected_icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                label="Eliminar Fondo",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.DRIVE_FILE_RENAME_OUTLINE,
                selected_icon=ft.Icons.DRIVE_FILE_RENAME_OUTLINE,
                label="Renombrar",
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