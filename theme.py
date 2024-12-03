import flet as ft

def configurar_ventana(page: ft.Page):
    """Configura las propiedades principales de la ventana."""
    page.title = "File Stuff"
    page.window.width = 800
    page.window.height = 600
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_800
    page.theme_mode = ft.ThemeMode.DARK

def configurar_tema():
    """Crea y devuelve un tema personalizado."""
    return ft.Theme(
        color_scheme_seed=ft.Colors.PURPLE,
        visual_density=ft.VisualDensity.COMFORTABLE,
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE,
            secondary=ft.Colors.RED,
            background=ft.Colors.GREY_900,
            surface=ft.Colors.GREY_800,
        ),
    )