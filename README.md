# Calculadora
Calculadora básica elaborada en Python con Tkinter

📌 Descripción
Este proyecto consiste en una calculadora básica desarrollada en Python con interfaz gráfica utilizando Tkinter.
Permite realizar operaciones matemáticas simples como suma, resta, multiplicación y división, y fue diseñado como proyecto académico con fines de aprendizaje.

🚀 Características
  1. Interfaz gráfica amigable con botones numéricos y de operaciones.
  2. Funciones básicas de calculadora (suma, resta, multiplicación, división).
  3. Función de limpiar pantalla.
  4. Manejo de errores básicos (ejemplo: división entre cero).
  5. Posibilidad de ampliación (nuevas funciones matemáticas).

🚀 Tecnologías utilizadas
  • Python 3.14
  • Tkinter (para la GUI)
  • PyInstaller (para la creación del ejecutable .exe)

📂 Estructura del proyecto
  Calculadora/
  │── src/
  │   └── calculadora.py
  │── assets/
  │   └── calculadora.ico
  │── README.md

📖 Instrucciones de uso
  1. Clonar el repositorio o descargar los archivos.
  2. Ejecutar el archivo calculadora.py:
      python calculadora.py
  3. Para usar la versión compilada en Windows, abrir el ejecutable ubicado en la carpeta dist/ (no incluido en este repositorio, se genera con   PyInstaller).

⚙️ Cómo compilar el ejecutable
  1. Si deseas generar tu propio .exe:
        pyinstaller --onefile --noconsole --name=Calculadora --icon=assets/calculadora.ico calculadora.py
  2. El ejecutable se guardará en la carpeta dist/.

✨ Posibles mejoras
  • Agregar más operaciones matemáticas (potencias, raíces, logaritmos).
  • Implementar un historial de operaciones.
  • Mejorar el diseño visual de la interfaz.
  • Adaptar la aplicación para Android o Web.

👨‍💻 Autor
  Proyecto desarrollado por Iván Narciso Guzmán Hernández como práctica académica/personal y para fortalecer habilidades en Python y desarrollo de interfaces gráficas.
