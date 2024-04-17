'''Genere una clase donde se instancie una comida rápida “hamburguesa” que
pueda ser entregada en mostrador, retirada por el cliente o enviada por
delivery. A los efectos prácticos bastará que la clase imprima el método de
entrega'''
class ComidaRapida:
    def entregar(self):
        pass

class EntregaMostrador(ComidaRapida):
    def entregar(self):
        print('La comida será entregada en el mostrador.')

class EntregaCliente(ComidaRapida):
    def entregar(self):
        print('La comida será retirada por el cliente.')

class EntregaDelivery(ComidaRapida):
    def entregar(self):
        print('La comida será enviada por delivery.')

class ComidaRapidaFactory:
    @staticmethod
    def crear_comida_rapida(metodo_entrega):
        if metodo_entrega == 'mostrador':
            return EntregaMostrador()
        elif metodo_entrega == 'cliente':
            return EntregaCliente()
        elif metodo_entrega == 'delivery':
            return EntregaDelivery()
        else:
            print('Método de entrega no válido.')
            return None

# Uso de la clase
factory = ComidaRapidaFactory()

# Interacción con el usuario para elegir el método de entrega
opcion = input("Elija el método de entrega (mostrador, retirada por el cliente, delivery): ")

# Creación de la comida rápida según la opción elegida por el usuario
comida_rapida = factory.crear_comida_rapida(opcion)
if comida_rapida is not None:
    comida_rapida.entregar()  # Imprime el método de entrega elegido por el usuario


