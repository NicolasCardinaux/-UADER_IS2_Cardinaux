'''Represente la lista de piezas componentes de un ensamblado con sus relaciones jerárquicas. 
Empiece con un producto principal formado por tres sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. 
Genere clases que representen esa configuración y la muestren. Luego agregue un sub- conjunto opcional adicional 
también formado por cuatro piezas. (Use el patrón composite).'''
# Clase abstracta "Componente"
class Componente:
    def mostrar(self):
        pass

# Clase concreta "Pieza"
class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        return self.nombre

# Clase concreta "Subconjunto"
class Subconjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self):
        resultado = self.nombre + " contiene:\n"
        for componente in self.componentes:
            resultado += "- " + componente.mostrar() + "\n"
        return resultado

# Crear subconjuntos y piezas
subconjunto1 = Subconjunto("Subconjunto 1")
subconjunto2 = Subconjunto("Subconjunto 2")
subconjunto3 = Subconjunto("Subconjunto 3")
subconjuntoOpcional = Subconjunto("Subconjunto Opcional")

for i in range(1, 5):
    subconjunto1.agregar(Pieza(f"Pieza {i}"))
    subconjunto2.agregar(Pieza(f"Pieza {i}"))
    subconjunto3.agregar(Pieza(f"Pieza {i}"))
    subconjuntoOpcional.agregar(Pieza(f"Pieza {i}"))

# Crear producto principal y agregar subconjuntos
productoPrincipal = Subconjunto("Producto Principal")
productoPrincipal.agregar(subconjunto1)
productoPrincipal.agregar(subconjunto2)
productoPrincipal.agregar(subconjunto3)

# Mostrar producto principal
print(productoPrincipal.mostrar())

# Agregar subconjunto opcional y mostrar producto principal
productoPrincipal.agregar(subconjuntoOpcional)
print(productoPrincipal.mostrar())
