'''Genere una clase donde se instancie una comida rápida “hamburguesa” que
pueda ser entregada en mostrador, retirada por el cliente o enviada por
delivery. A los efectos prácticos bastará que la clase imprima el método de
entrega'''

class ComidaRapida:
    def __init__(self, metodo_entrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        print(f'La comida será entregada por: {self.metodo_entrega}')


class ComidaRapidaFactory:
    @staticmethod
    def crear_comida_rapida(metodo_entrega):
        return ComidaRapida(metodo_entrega)


# Uso de la clase
factory = ComidaRapidaFactory()

# Interacción con el usuario para elegir el método de entrega
opcion = input("Elija el método de entrega (mostrador, retirada por el cliente, delivery): ")

# Creación de la comida rápida según la opción elegida por el usuario
comida_rapida = factory.crear_comida_rapida(opcion)
comida_rapida.entregar()  # Imprime el método de entrega elegido por el usuario


