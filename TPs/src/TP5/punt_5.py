'''Modifique el programa IS2_taller_memory.py para que la clase tenga la capacidad de almacenar
hasta 4 estados en el pasado y pueda recuperar los mismos en cualquier orden de ser necesario.
El método undo deberá tener un argumento adicional indicando si se desea recuperar el 
inmediato anterior (0) y los anteriores a el (1,2,3).'''
import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def __init__(self):
        self.saved_states = []

    def save(self, writer):
        # Guarda el estado actual al principio de la lista
        self.saved_states.insert(0, writer.save())

        # Asegura que solo se guarden los últimos 4 estados
        if len(self.saved_states) > 4:
            self.saved_states.pop()

    def undo(self, writer, state_index):
        if state_index < len(self.saved_states):
            writer.undo(self.saved_states[state_index])

if __name__ == "__main__":
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("se invoca al <undo> para el estado 0")
    caretaker.undo(writer, 0)

    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> para el estado 1")
    caretaker.undo(writer, 1)

    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
