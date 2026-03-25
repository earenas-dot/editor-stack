# se importa Stack porque undo y redo deben usar una estructura de pila propia
from stack import Stack


# clase que contiene toda la lógica del editor separada de la interfaz
class TextEditor:

    def __init__(self):

        # almacena el texto actual del editor
        self.content = ""

        # pila que guarda acciones realizadas para poder deshacerlas
        self.undo_stack = Stack()

        # pila que guarda acciones deshechas para poder rehacerlas
        self.redo_stack = Stack()

        # lista que almacena historial de acciones realizadas
        self.history_log = []


    def write(self, text):

        # evita escribir texto vacío
        if text.strip() == "":
            raise ValueError("No puede escribir texto vacío")

        # se guarda la acción como tupla para poder revertirla después
        action = ("write", text)

        # se guarda la acción en la pila undo siguiendo LIFO
        self.undo_stack.push(action)

        # al escribir algo nuevo, redo pierde validez
        self.redo_stack.clear()

        # concatena texto al contenido actual
        self.content += text

        # guarda registro en historial
        self.history_log.append(f"write('{text}')")


    def delete(self, n):

        # verifica que n sea número entero
        if not isinstance(n, int):
            raise TypeError("Debe ingresar un número entero")

        # evita borrar valores negativos o cero
        if n <= 0:
            raise ValueError("Debe borrar al menos 1 carácter")

        # evita borrar más caracteres de los que existen
        if n > len(self.content):
            raise ValueError("No hay suficientes caracteres para borrar")

        # guarda texto eliminado para poder restaurarlo con undo
        deleted_text = self.content[-n:]

        # guarda acción delete para posible reversión
        action = ("delete", deleted_text)

        # almacena acción en pila undo
        self.undo_stack.push(action)

        # limpiar redo porque hay nueva acción
        self.redo_stack.clear()

        # elimina los últimos n caracteres
        self.content = self.content[:-n]

        # guarda acción en historial
        self.history_log.append(f"delete({n})")


    def undo(self):

        # evita deshacer cuando no hay acciones
        if self.undo_stack.is_empty():
            raise Exception("No hay acciones para deshacer")

        # obtiene última acción realizada
        action = self.undo_stack.pop()

        # si la acción fue escribir
        if action[0] == "write":

            text = action[1]

            # elimina texto agregado
            self.content = self.content[:-len(text)]

        # si la acción fue borrar
        elif action[0] == "delete":

            text = action[1]

            # vuelve a agregar texto eliminado
            self.content += text

        # acción pasa a pila redo
        self.redo_stack.push(action)

        # registrar acción en historial
        self.history_log.append("undo()")


    def redo(self):

        # evita rehacer cuando no hay acciones deshechas
        if self.redo_stack.is_empty():
            raise Exception("No hay acciones para rehacer")

        # obtiene acción deshecha
        action = self.redo_stack.pop()

        # reaplica acción write
        if action[0] == "write":

            self.content += action[1]

        # reaplica acción delete
        elif action[0] == "delete":

            self.content = self.content[:-len(action[1])]

        # vuelve a guardar acción en pila undo
        self.undo_stack.push(action)

        # registrar acción en historial
        self.history_log.append("redo()")


    def show(self):

        # devuelve contenido actual
        return self.content


    def history(self):

        # devuelve lista de acciones realizadas
        return self.history_log