## FILES STUFF

![file-stuff](https://github.com/user-attachments/assets/91bc7b6a-9263-4584-b142-4ead1a5e1e0b)

- Versión 0.03

Corregidos algunos errores a la hora de crear el entorno virtual en Windows en el que se ejecuta el programa. También se ha añadido el icono de la bandeja del sistema. Este icono en Linux no funciona como debería ya que pystray tiene ciertas limitaciones con Wayland y Xorg.

- Versión 0.04

Se han añadido nuevas funcionalidades como son la de Convertir archivo PDF en archivos docx. La conversión a archivos odt todavía no es funcional. También se ha añadido la posibilidad de fusionar diferentes archivos PDF contenidos en una carpeta en un solo archivo PDF. Además se han realizado algunas correcciones menores.

- Versión 0.05

Se ha realizado la una modularización del programa. Las funcionalidades se han puesto en la carpeta functionalities, las funciones relacionadas con cada funcionalidad se han colocado en la carpeta functions, y las vistas de cada una de las funcionalidades se han colocado en la carpeta views.

- Versión 0.06

Añadidas nuevas funcionalidades para convertir una imagen a diferentes formatos (png,jpeg,gif,bmp y webp), para eliminar el fondo de las imágenes contenidas dentro de una carpeta utilizando rembg y onnxruntime, y también se ha añadido la posibilidad de renombrar TODOS los archivos que estén incluidos dentro de una carpeta (permite utilizar el comodín ### para poder renombrar archivos hasta el 999)

- Versión 0.005

Este proyecto es una aplicación de escritorio que permite gestionar archivos de manera eficiente, enfocándose en la eliminación de archivos duplicados y la organización de archivos en carpetas. La aplicación está construida utilizando el framework Flet para la interfaz gráfica y poco a poco voy a ir añadiéndole más cosas que me pueda ir haciendo falta.

## Características

- Eliminar Archivos Duplicados: Escanea una carpeta para encontrar y eliminar archivos duplicados.
- Organizar Archivos: Organiza los archivos dentro de una carpeta de acuerdo con su tipo o nombre.
- Redimensionar Imágenes: Redimensiona imágenes de una en una. 
- Convertir Imágenes: Permite seleccionar una imagen y convertirla a otro formato (png, jpeg, gif, bmp, webp)
- Eliminar Fondo: Esta opción permite seleccionar una carpeta para eliminar el fondo de las imágenes.
- Renombrado Archivos: Permite renombrar masivamente los archivos de una carpeta.
- Convertir PDFs: Esta opción nos da la posibilidad de convertir archivos PDF en archivos docx.
- Fusionar PDFs: Con esta opción podremos juntar los PDF contenidos en en una carpeta en un solo PDF.

## Requisitos 

- En Linux es necesario tener instalado python3-venv para crear el entorno virtual en el que se ejecutará el programa. Se instalará de manera automática en caso de que no esté instalado en el sistema. Aun que para ello será necesario que el usuario proporcione su contraseña.

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
