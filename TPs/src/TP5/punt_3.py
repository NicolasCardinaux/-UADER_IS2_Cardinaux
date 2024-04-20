'''Implemente una clase bajo el patrón observer donde una serie de clases están subscriptas, 
cada clase espera que su propio ID (una secuencia arbitraria de 4 caracteres) sea expuesta y 
emitirá un mensaje cuando el ID emitido y el propio coinciden. Implemente 4 clases de tal 
manera que cada una tenga un ID especifico. Emita 8 ID asegurándose que al menos cuatro 
de ellos coincidan con ID para el que tenga una clase implementada.'''
class Observer:
    def __init__(self, id):
        self.id = id

    def update(self, id):
        if self.id == id:
            print(f"Observer {self.id}: Mi ID ha sido emitido")

class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit(self, id):
        for observer in self.observers:
            observer.update(id)

# Crear el sujeto
subject = Subject()

# Crear y suscribir los observadores
observer1 = Observer("ID01")
observer2 = Observer("ID02")
observer3 = Observer("ID03")
observer4 = Observer("ID04")

subject.subscribe(observer1)
subject.subscribe(observer2)
subject.subscribe(observer3)
subject.subscribe(observer4)

# Emitir IDs
ids = ["ID01", "ID05", "ID02", "ID06", "ID03", "ID07", "ID04", "ID08"]
for id in ids:
    subject.emit(id)
