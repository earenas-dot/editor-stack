# tkinter necesario para crear la ventana principal
import tkinter as tk

# se importa la interfaz gráfica
from ui import EditorGUI


def main():

    # crea ventana principal
    root = tk.Tk()

    # inicia la interfaz del editor
    app = EditorGUI(root)

    # mantiene ventana en ejecución
    root.mainloop()


# permite ejecutar el programa directamente
if __name__ == "__main__":

    main()