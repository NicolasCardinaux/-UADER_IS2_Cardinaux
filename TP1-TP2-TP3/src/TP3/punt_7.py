from abc import ABC, abstractmethod
class FabricaAbstracta(ABC):
    @abstractmethod
    def crear_comida(self):
        pass
    @abstractmethod
    def crear_bebida(self):
        pass
class FabricaItaliana(FabricaAbstracta):
    def crear_comida(self):
        return SpaghettiCarbonara()
    def crear_bebida(self):
        return VinoChianti()
class FabricaMexicana(FabricaAbstracta):
    def crear_comida(self):
        return Tacos()
    def crear_bebida(self):
        return Tequila()
class Comida(ABC):
    pass
class Bebida(ABC):
    pass
class SpaghettiCarbonara(Comida):
    pass
class VinoChianti(Bebida):
    pass
class Tacos(Comida):
    pass
class Tequila(Bebida):
    pass
def codigo_cliente(fabrica):
    comida = fabrica.crear_comida()
    bebida = fabrica.crear_bebida()
    print(f"Creado {comida.__class__.__name__} y {bebida.__class__.__name__}")
while True:
    print("Introduce el tipo de cocina (Italiana, Mexicana) o 'salir' para terminar:")
    cocina = input().strip()
    if cocina.lower() == 'salir':
        break
    elif cocina.lower() == 'italiana':
        codigo_cliente(FabricaItaliana())
    elif cocina.lower() == 'mexicana':
        codigo_cliente(FabricaMexicana())
    else:
        print("Cocina desconocida. Por favor, inténtalo de nuevo.")
