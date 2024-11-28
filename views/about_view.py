import flet as ft

def abrir_repositorio(page: ft.Page):
    # Función que abre el enlace en el navegador por defecto del sistema
    page.launch_url("https://github.com/sapoclay/file-stuff")

def view_about(page: ft.Page):
    # Vista de información con el contenido centrado
    return ft.Container(
        content=ft.Column(
            [
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
                    on_click=lambda _: abrir_repositorio(page),  # Enlaza con la función para abrir el repositorio
                ),
                ft.Text(
                    "entreunosyceros.net",
                    size=14,
                    color=ft.Colors.GREY_600,  
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centra los elementos verticalmente dentro de la columna
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra horizontalmente los elementos dentro de la columna
        ),
        padding=30,
        expand=True,  # Asegura que el contenedor ocupe todo el espacio disponible
    )
