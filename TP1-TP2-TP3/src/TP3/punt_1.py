'''Provea una clase que dado un número entero cualquiera retorne el factorial del
mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
instancia de clase.'''
class SingletonMath:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonMath, cls).__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def factorial(self, n):
        if n in self._cache:
            return self._cache[n]
        elif n == 0:
            return 1
        else:
            self._cache[n] = n * self.factorial(n - 1)
            return self._cache[n]

# Uso de la clase
singleton = SingletonMath()

# Solicita un valor al usuario
valor = int(input("Por favor, introduce un número entero: "))

# Calcula y muestra el factorial del valor introducido
print(singleton.factorial(valor))
