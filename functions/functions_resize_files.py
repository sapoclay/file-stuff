import flet as ft
from functionalities.resize_files import batch_resize

def resize_images(state, resize_result_text, width_field, height_field):
    try:
        input_folder = state.get("resize_input_folder", "")
        output_folder = state.get("resize_output_folder", "")

        if not input_folder or not output_folder:
            resize_result_text.value = "Error!! Selecciona las carpetas de entrada y salida."
            resize_result_text.color = ft.Colors.RED_500
            resize_result_text.update()
            return

        width = int(width_field.value)
        height = int(height_field.value)

        if width <= 0 or height <= 0:
            resize_result_text.value = "Error!! Las dimensiones deben ser mayores que 0."
            resize_result_text.color = ft.Colors.RED_500
            resize_result_text.update()
            return

        batch_resize(state["resize_input_folder"], state["resize_output_folder"], width, height)
        resize_result_text.value = "Imágenes redimensionadas correctamente!!"
        resize_result_text.color = ft.Colors.GREEN_500
        resize_result_text.update()
    except ValueError:
        resize_result_text.value = "Error!! Ingresa dimensiones válidas. SOLO NÚMEROS MAYORES QUE 0."
        resize_result_text.color = ft.Colors.RED_500
        resize_result_text.update()
    except Exception as e:
        resize_result_text.value = f"Error al redimensionar: {str(e)}"
        resize_result_text.color = ft.Colors.RED_500
        resize_result_text.update()
