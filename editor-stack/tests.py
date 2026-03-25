# se importa Stack para probar su funcionamiento
from stack import Stack

# se importa el editor para probar undo y redo
from editor import TextEditor


def test_stack():

    # crear pila
    s = Stack()

    # agregar elementos
    s.push(10)

    s.push(20)

    # verificar tamaño
    assert s.size() == 2

    # verificar LIFO
    assert s.pop() == 20

    # verificar elemento superior
    assert s.peek() == 10

    # verificar que no está vacía
    assert not s.is_empty()


def test_editor():

    # crear editor
    e = TextEditor()

    # escribir texto
    e.write("Hola")

    assert e.show() == "Hola"

    # escribir más texto
    e.write(" Mundo")

    assert e.show() == "Hola Mundo"

    # deshacer última acción
    e.undo()

    assert e.show() == "Hola"

    # rehacer acción
    e.redo()

    assert e.show() == "Hola Mundo"

    # borrar caracteres
    e.delete(5)

    assert e.show() == "Hola "


def test_limits():

    e = TextEditor()

    # probar undo sin acciones
    try:

        e.undo()

    except:

        assert True

    # probar borrar más caracteres de los existentes
    try:

        e.delete(10)

    except:

        assert True


if __name__ == "__main__":

    # ejecutar pruebas
    test_stack()

    test_editor()

    test_limits()

    print("Todas las pruebas pasaron")