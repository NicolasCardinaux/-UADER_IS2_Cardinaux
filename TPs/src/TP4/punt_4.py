'''4.	Implemente una clase que permita a un número cualquiera imprimir su valor, 
luego agregarle sucesivamente.
a.	Sumarle 2.
b.	Multiplicarle por 2.
c.	Dividirlo por 3.
Mostrar los resultados de la clase sin agregados y con la invocación anidada a las clases 
con las diferentes operaciones. Use un patrón decorator para implementar.
'''
class Number:
    def __init__(self, value):
        self._value = value

    def operation(self):
        return self._value

class NumberDecorator(Number):
    def __init__(self, number):
        self._number = number

# Clase decoradora para sumarle 2 al número
class AddTwo(NumberDecorator):
    def operation(self):
        return self._number.operation() + 2

# Clase decoradora para multiplicar por 2 al número
class MultiplyByTwo(NumberDecorator):
    def operation(self):
        return self._number.operation() * 2

# Clase decoradora para dividir por 3 al número
class DivideByThree(NumberDecorator):
    def operation(self):
        return self._number.operation() / 3

# Crear un número inicial
num = Number(5)
print(num.operation())  # Imprime: 5

# Aplicar las operaciones secuencialmente
num = AddTwo(num)
print(num.operation())  # Imprime: 7

num = MultiplyByTwo(num)
print(num.operation())  # Imprime: 14

num = DivideByThree(num)
print(num.operation())  # Imprime: 4.666666666666667
