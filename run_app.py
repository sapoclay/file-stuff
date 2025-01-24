import os
import subprocess
import sys


# Obtener el directorio donde se encuentra el archivo run_app.py
DIRECTORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# Nombre del entorno virtual
VENV_DIR = os.path.join(DIRECTORIO_SCRIPT, "venv")

# Determinar el ejecutable de Python dentro del entorno virtual
def obtener_python_ejecutable():
    if os.name == 'nt':  # Windows
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:  # Linux/macOS
        return os.path.join(VENV_DIR, "bin", "python")

# Verificar si pip está instalado; instalarlo si no lo está
def asegurar_pip(python_executable):
    try:
        subprocess.run([python_executable, "-m", "pip", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("pip no está instalado. Intentando instalar pip manualmente...")
        subprocess.run([python_executable, "-m", "ensurepip", "--upgrade"], check=True)

# Crear el entorno virtual usando venv
def crear_entorno_virtual():
    print("Creando el entorno virtual con venv...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)

# Instalar las dependencias desde requirements.txt
def instalar_dependencias(python_executable):
    print("Instalando dependencias...")
    asegurar_pip(python_executable)
    
    ruta_requirements = os.path.join(DIRECTORIO_SCRIPT, "requirements.txt")
    
    if os.path.exists(ruta_requirements):
        subprocess.run([python_executable, "-m", "pip", "install", "-r", ruta_requirements], check=True)
    else:
        print("No se encontró el archivo requirements.txt. Asegúrate de que esté en el directorio del script.")

# Ejecutar el script principal dentro del entorno virtual
def ejecutar_app():
    python_executable = obtener_python_ejecutable()
    ruta_main = os.path.join(DIRECTORIO_SCRIPT, "app.py")
    
    if os.path.isfile(python_executable):
        subprocess.run([python_executable, ruta_main], check=True)
    else:
        print(f"El ejecutable no se encuentra: {python_executable}")

# Instalar paquetes necesarios en Linux automáticamente (opcional)
def instalar_paquetes_linux():
    if os.name == 'posix' and sys.platform == 'linux':
        try:
            subprocess.run(["sudo", "apt", "install", "-y", "python3-venv"], check=True)
        except Exception as e:
            print(f"Error al instalar python3-venv: {e}")

# Lógica principal
def main():
    python_executable = obtener_python_ejecutable()

    # Instalar herramientas necesarias en Linux (opcional)
    if os.name == 'posix' and sys.platform == 'linux':
        instalar_paquetes_linux()

    # Verificar si el entorno virtual existe
    if not os.path.isdir(VENV_DIR):
        print("El entorno virtual no existe. Creando uno nuevo...")
        try:
            crear_entorno_virtual()
        except Exception as e:
            print(f"Error al crear el entorno virtual: {e}")
            sys.exit(1)

    # Instalar dependencias
    try:
        instalar_dependencias(python_executable)
    except Exception as e:
        print(f"Error al instalar dependencias: {e}")
        sys.exit(1)

    # Ejecutar la aplicación
    try:
        ejecutar_app()
    except Exception as e:
        print(f"Error al ejecutar la aplicación: {e}")
        sys.exit(1)

# Ejecutar el script
if __name__ == "__main__":
    main() 