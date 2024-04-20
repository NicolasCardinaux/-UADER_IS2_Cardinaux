'''Implemente una clase bajo el patrón iterator que almacene una cadena de caracteres
 y permita recorrerla en sentido directo y reverso.'''
class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.string):
            result = self.string[self.index]
            self.index += 1
            return result
        raise StopIteration

class ReverseStringIterator(StringIterator):
    def __init__(self, string):
        super().__init__(string)
        self.index = len(string)

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.string[self.index]
        raise StopIteration

# Pedir al usuario que ingrese la cadena
cadena = input("Por favor, ingrese una cadena de caracteres: ")

# Crear los iteradores
iterator = StringIterator(cadena)
reverse_iterator = ReverseStringIterator(cadena)

# Recorrer la cadena en sentido directo
print("Sentido directo:")
for char in iterator:
    print(char)

# Recorrer la cadena en sentido reverso
print("\nSentido reverso:")
for char in reverse_iterator:
    print(char)
