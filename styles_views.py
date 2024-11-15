import flet as ft

# Función para aplicar estilo de título común
def create_title(text):
    return ft.Container(
        content=ft.Text(
            text,
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE_200,
        ),
        margin=ft.margin.only(bottom=20)
    )

# Función para crear contenedor con padding y expand=True
def create_container_with_padding(content):
    return ft.Container(
        content=content,
        padding=30,
        expand=True
    )

# Función para crear botones elevados comunes
def create_elevated_button(text, icon, on_click):
    return ft.ElevatedButton(
        text=text,
        icon=icon,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_900,
        on_click=on_click,
    )

# Función de estilo de contenedor con borde y fondo
def container_border_style():
    return {
        "border": ft.border.all(2, ft.colors.BLUE_400),
        "border_radius": 10,
        "padding": 20,
        "bgcolor": ft.colors.GREY_800
    }

# Función para el estilo del texto en botones
def button_style():
    return {
        "color": ft.colors.WHITE,
        "bgcolor": ft.colors.BLUE_900
    }

# Función para aplicar el estilo de un texto de título
def title_text_style():
    return ft.Text(
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_200
    )

# Estilo para los textos de las carpetas seleccionadas
def folder_selection_text_style(text):
    return ft.Text(
        text,
        size=14,
        color=ft.colors.BLUE_200
    )

# Estilo de los resultados
def result_text_style():
    return ft.Text(
        "Resultado del redimensionado se mostrará aquí",
        color=ft.colors.BLUE_200,
        weight=ft.FontWeight.BOLD,
        size=16,
        expand=True
        ),