'''Cree una clase bajo el patrón cadena de responsabilidad donde los números del
1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que identifique 
la necesidad de consumir el número lo hará y caso contrario lo pasará al siguiente en la cadena. 
Implemente una clase que consuma números primos y otra números pares. Puede ocurrir que un número
no sea consumido por ninguna clase en cuyo caso se marcará como no consumido.
'''
class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, number):
        if self.next_handler:
            return self.next_handler.handle(number)

class PrimeHandler(Handler):
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"PrimeHandler: Consumió {number} (primo)")
        elif self.next_handler:
            return self.next_handler.handle(number)

class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"EvenHandler: Consumió {number} (par)")
        elif self.next_handler:
            return self.next_handler.handle(number)

class UnhandledHandler(Handler):
    def handle(self, number):
        print(f"UnhandledHandler: {number} no fue consumido")

# Crear los manejadores
prime_handler = PrimeHandler()
even_handler = EvenHandler()
unhandled_handler = UnhandledHandler()

# Establecer la cadena de responsabilidad
prime_handler.set_next(even_handler).set_next(unhandled_handler)

# Pasar los números del 1 al 100 a través de la cadena de responsabilidad
for number in range(1, 101):
    prime_handler.handle(number)
