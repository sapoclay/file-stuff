import flet as ft
from state import state

def build_navigation_rail(content_area, duplicate_file_view, organize_files_view, bulk_rename_view, resize_image_view):
    # Lógica para cambiar la vista
    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            state["current_view"] = "duplicates"
            content_area.content = duplicate_file_view
        elif selected == 1:
            state["current_view"] = "organize"
            content_area.content = organize_files_view
        elif selected == 2:
            state["current_view"] = "rename"
            content_area.content = bulk_rename_view
        elif selected == 3:
            state["current_resize"] = "resize"
            content_area.content = resize_image_view
        elif selected == 4:
            state["current_view"] = "coming_soon"
            content_area.content = ft.Text(value="Próximamente....", size=24)
        content_area.update()

    # Configuración del NavigationRail
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.DELETE_FOREVER,
                selected_icon=ft.icons.DELETE_FOREVER,
                label="Duplicados",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FOLDER_COPY,
                selected_icon=ft.icons.FOLDER_COPY,
                label="Organizar",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE, 
                selected_icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE, 
                label="Renombrar Archivos",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.IMAGE, 
                selected_icon=ft.icons.IMAGE, 
                label="Redimensionar Imágenes",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.icons.ADD_CIRCLE,
                label="Próximamente",
            )
        ],
        on_change=change_view,
        bgcolor=ft.colors.GREY_900,
    )
    
    return rail
