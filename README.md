## FILES STUFF

![file-stuff](https://github.com/user-attachments/assets/91bc7b6a-9263-4584-b142-4ead1a5e1e0b)

- Versión 0.005

Este proyecto es una aplicación de escritorio que permite gestionar archivos de manera eficiente, enfocándose en la eliminación de archivos duplicados, la organización de archivos en carpetas, convertir imágenes de un formato a otro y el redimensionamiento de imágenes. La aplicación está construida utilizando el framework Flet para la interfaz gráfica y poco a poco voy a ir añadiéndole más cosas que me pueda ir haciendo falta.

- Versión 0.5

Se ha realizado la una modularización del programa. Las funcionalidades se han puesto en la carpeta functionalities, las funciones relacionadas con cada funcionalidad se han colocado en la carpeta functions, y las vistas de cada una de las funcionalidades se han colocado en la carpeta views.

- Versión 0.4

Añadidas nuevas funcionalidades para convertir una imagen a diferentes formatos (png,jpeg,gif,bmp y webp), para eliminar el fondo de las imágenes contenidas dentro de una carpeta utilizando rembg y onnxruntime, y también se ha añadido la posibilidad de renombrar TODOS los archivos que estén incluidos dentro de una carpeta (permite utilizar el comodín ### para poder renombrar archivos hasta el 999)

## Características

- Eliminar Archivos Duplicados: Escanea una carpeta para encontrar y eliminar archivos duplicados.
- Organizar Archivos: Organiza los archivos dentro de una carpeta de acuerdo con su tipo o nombre.
- Redimensionar Imágenes: Redimensiona imágenes de una en una. 
- Convertir Imágenes: Permite seleccionar una imagen y convertirla a otro formato (png, jpeg, gif, bmp, webp)
- Eliminar Fondo: Esta opción permite seleccionar una carpeta para eliminar el fondo de las imágenes.
- Renombrado Archivos: Permite renombrar masivamente los archivos de una carpeta.


## Ejecutar la aplicación

```
git clone https://github.com/sapoclay/file-stuff

cd file-stuff
```

Las dependencias deberían instalarse de forma automática dentro del entorno virtual que se va a crear al ejecutar el archivo:

```
python3 run_app.py
```

>[!NOTE]
>Al ejecutar por primera vez el programa, va a tardar un poco en iniciarse, ya que debe crear el entorno virtual e instalar las dependencias necesarias.
>En las siguientes ejecuciones ya será mucho más rápido.
