# Text Editor con Stack (Undo/Redo)

## Descripción
Este proyecto simula un editor de texto simple usando la estructura de datos Stack.
Permite escribir texto, borrar caracteres, deshacer y rehacer acciones.

El proyecto demuestra el uso del principio LIFO (Last In First Out).

## Requisitos
Python 3.12 o superior
Python 3.14 utilizado

Tkinter (incluido en Python)

## Cómo ejecutar

1. Descargar el proyecto o clonar repositorio
2. Abrir carpeta en Visual Studio Code
3. Ejecutar:

python main.py

## Funcionalidades
write(text)
delete(n)
undo()
redo()
history()

## Estructura
stack.py → implementación de pila
editor.py → lógica del editor
ui.py → interfaz gráfica
main.py → ejecución del programa
tests.py → pruebas básicas

## Pruebas
Ejecutar:

python tests.py

Si no hay errores, las pruebas funcionan correctamente.# editor-stack
Simulador de editor con historial de acciones usando pilas
