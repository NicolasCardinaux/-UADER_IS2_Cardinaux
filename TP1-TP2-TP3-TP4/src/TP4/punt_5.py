'''5.	Imagine una situación donde pueda ser de utilidad el patrón “flyweight”.
Un ejemplo podría ser una cafetería que vende diferentes tipos de café. 
ada tipo de café tiene un sabor, pero muchos atributos, como la taza, la cuchara, 
la servilleta, son comunes y pueden ser compartidos entre diferentes tipos de café.
'''
class Coffee:
    def __init__(self, flavor):
        self.flavor = flavor

class CoffeeFactory:
    _coffees = dict()

    def get_coffee(self, flavor):
        if flavor not in self._coffees:
            self._coffees[flavor] = Coffee(flavor)
        return self._coffees[flavor]

# Uso del patrón Flyweight
factory = CoffeeFactory()

orders = ['espresso', 'cappuccino', 'espresso', 'latte']
coffees = [factory.get_coffee(order) for order in orders]

# Imprime los objetos de café
for i, coffee in enumerate(coffees):
    print(f"Coffee {i+1}: {coffee.flavor}")
