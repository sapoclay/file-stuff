import flet as ft

def configure_theme():
    return ft.Theme(
        color_scheme_seed=ft.colors.PURPLE,
        visual_density=ft.VisualDensity.COMFORTABLE,
        color_scheme=ft.ColorScheme(
            primary=ft.colors.PURPLE,
            secondary=ft.colors.BLUE,
            background=ft.colors.GREY_900,
            surface=ft.colors.GREY_800,
        )
    )
