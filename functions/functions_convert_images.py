def convert_image_function(state, convert_input_text, format_dropdown, convert_result_text):
    try:
        if not state["convert_input_file"]:
            convert_result_text.value = "ERROR!! Selecciona una imagen"
            convert_result_text.color = "RED"
            convert_result_text.update()
            return
        if not format_dropdown.value:
            convert_result_text.value = "ERROR!! Selecciona un formato de salida válido"
            convert_result_text.color = "RED"
            convert_result_text.update()
            return
        from functionalities.converter_images import convert_img
        convert_img(state["convert_input_file"], format_dropdown.value)
        convert_result_text.value = "Imagen convertida exitosamente!!!"
        convert_result_text.color = "GREEN"
        convert_result_text.update()
    except Exception as e:
        convert_result_text.value = f"ERROR al convertir la imagen: {str(e)}"
        convert_result_text.color = "RED"
        convert_result_text.update()