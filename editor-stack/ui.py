# tkinter se usa porque permite crear interfaz gráfica sin instalar librerías externas
import tkinter as tk

# messagebox permite mostrar errores al usuario sin cerrar el programa
from tkinter import messagebox

# se importa la lógica del editor separada de la interfaz
from editor import TextEditor


class EditorGUI:

    def __init__(self, root):

        # instancia del editor para manejar la lógica
        self.editor = TextEditor()

        # título de la ventana
        root.title("Editor con Stack (Undo/Redo)")

        # tamaño de la ventana
        root.geometry("600x500")

        # área donde se muestra el texto actual
        self.text_area = tk.Text(root, height=10, width=60)

        self.text_area.pack(pady=10)

        # campo para ingresar texto a escribir
        self.input_text = tk.Entry(root, width=40)

        self.input_text.pack()

        # botón que ejecuta write
        btn_write = tk.Button(root, text="Write", command=self.write_text)

        btn_write.pack(pady=5)

        # campo para ingresar número de caracteres a borrar
        self.delete_input = tk.Entry(root, width=10)

        self.delete_input.pack()

        # botón que ejecuta delete
        btn_delete = tk.Button(root, text="Delete N", command=self.delete_text)

        btn_delete.pack(pady=5)

        # botón que ejecuta undo
        btn_undo = tk.Button(root, text="Undo", command=self.undo)

        btn_undo.pack(pady=5)

        # botón que ejecuta redo
        btn_redo = tk.Button(root, text="Redo", command=self.redo)

        btn_redo.pack(pady=5)

        # botón que muestra historial
        btn_history = tk.Button(root, text="Mostrar historial", command=self.show_history)

        btn_history.pack(pady=5)


    def update_text(self):

        # borra contenido visual anterior
        self.text_area.delete("1.0", tk.END)

        # inserta contenido actualizado
        self.text_area.insert(tk.END, self.editor.show())


    def write_text(self):

        try:

            # obtiene texto ingresado por el usuario
            text = self.input_text.get()

            # ejecuta función write del editor
            self.editor.write(text)

            # actualiza texto mostrado
            self.update_text()

            # limpia campo de entrada
            self.input_text.delete(0, tk.END)

        except Exception as e:

            # muestra error si ocurre problema
            messagebox.showerror("Error", str(e))


    def delete_text(self):

        try:

            # convierte entrada a entero
            n = int(self.delete_input.get())

            # ejecuta función delete
            self.editor.delete(n)

            # actualiza texto mostrado
            self.update_text()

            # limpia campo
            self.delete_input.delete(0, tk.END)

        except Exception as e:

            messagebox.showerror("Error", str(e))


    def undo(self):

        try:

            # ejecuta undo
            self.editor.undo()

            self.update_text()

        except Exception as e:

            messagebox.showerror("Error", str(e))


    def redo(self):

        try:

            # ejecuta redo
            self.editor.redo()

            self.update_text()

        except Exception as e:

            messagebox.showerror("Error", str(e))


    def show_history(self):

        # convierte historial en texto con saltos de línea
        history_text = "\n".join(self.editor.history())

        # muestra historial en ventana emergente
        messagebox.showinfo("Historial", history_text)