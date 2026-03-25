# Clase Stack creada manualmente porque la tarea exige implementar la estructura de datos propia
class Stack:

    def __init__(self):
        # lista interna porque permite almacenar elementos dinámicamente
        self._items = []

    def push(self, item):
        # append agrega elemento al final, representando la cima de la pila (LIFO)
        self._items.append(item)

    def pop(self):
        # validación para evitar extraer elementos cuando la pila está vacía
        if self.is_empty():
            raise IndexError("La pila está vacía")
        
        # pop elimina el último elemento agregado (LIFO)
        return self._items.pop()

    def peek(self):
        # permite consultar el último elemento sin eliminarlo
        if self.is_empty():
            return None
        
        # [-1] accede al último elemento de la lista
        return self._items[-1]

    def is_empty(self):
        # verifica si la pila está vacía
        return len(self._items) == 0

    def size(self):
        # devuelve la cantidad de elementos en la pila
        return len(self._items)

    def clear(self):
        # se usa para limpiar la pila redo cuando se realiza una nueva acción
        self._items.clear()

    def __repr__(self):
        # representación en texto útil para depuración
        return str(self._items)