import os

def bulk_rename_files(directory, name_template, snack_bar):
    """
    Renombra archivos de forma masiva en el directorio especificado.

    :param directory: Ruta de la carpeta donde están los archivos.
    :param name_template: Plantilla de renombre, usa '###' para indicar el contador.
    :param snack_bar: El snack bar para mostrar mensajes de error.
    :return: Lista con los nombres nuevos de los archivos o mensaje de error en el snack bar.
    """
    try:
        # Validar que la plantilla contiene '###'
        if '###' not in name_template:
            snack_bar.content.value = "Error: La plantilla debe contener '###' para indicar la posición del contador."
            snack_bar.open = True
            return []

        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        renamed_files = []

        counter = 1
        for file in files:
            # Generar el nuevo nombre basado en la plantilla
            new_name = name_template.replace("###", str(counter).zfill(3))
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            
            os.rename(old_path, new_path)
            renamed_files.append(new_name)
            counter += 1

        return renamed_files

    except Exception as e:
        snack_bar.content.value = f"Error al renombrar archivos: {str(e)}"
        snack_bar.open = True
        return []
