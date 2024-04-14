'''Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho dispone de dos trenes laminadores,
 uno que genera planchas de 5 mts y otro de 10 mts. Genere una clase que represente a las 
 láminas en forma genérica al cual se le pueda indicar que a que tren laminador se enviará a producir. 
 (Use el patrón bridge en la solución).'''

# Clase abstracta "Lamina"
class Lamina:
    def __init__(self, laminador):
        self.laminador = laminador

    def producir(self):
        pass

# Clase concreta "LaminaAcero"
class LaminaAcero(Lamina):
    def __init__(self, laminador):
        super().__init__(laminador)

    def producir(self):
        return f"Lámina de acero de 0.5\" de espesor y 1.5 metros de ancho producida en {self.laminador.producir()}"

# Clase abstracta "Laminador"
class Laminador:
    def producir(self):
        pass

# Clase concreta "Laminador5Metros"
class Laminador5Metros(Laminador):
    def producir(self):
        return "tren laminador de 5 metros"

# Clase concreta "Laminador10Metros"
class Laminador10Metros(Laminador):
    def producir(self):
        return "tren laminador de 10 metros"

# Crear objetos de laminadores
laminador5Metros = Laminador5Metros()
laminador10Metros = Laminador10Metros()

# Crear objetos de láminas y asignarles un laminador
lamina1 = LaminaAcero(laminador5Metros)
lamina2 = LaminaAcero(laminador10Metros)

# Producir las láminas
print(lamina1.producir())
print(lamina2.producir())
