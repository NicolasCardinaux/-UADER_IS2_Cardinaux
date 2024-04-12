'''Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
deberá recibir un valor de importe base imponible y deberá retornar la suma
del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
esa base imponible.'''
class SingletonImpuesto:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonImpuesto, cls).__new__(cls)
        return cls._instance

    def calculate_impuestos(self, base_amount):
        IVA = 0.21
        IIBB = 0.05
        municipal_contributions = 0.012

        total_impuestos = base_amount * (IVA + IIBB + municipal_contributions)
        impuesto_vat = base_amount * IVA
        impuesto_income = base_amount * IIBB
        impuesto_municipal = base_amount * municipal_contributions
        return total_impuestos, impuesto_vat, impuesto_income, impuesto_municipal

# Uso de la clase
singleton = SingletonImpuesto()

# Solicita el valor al usuario
valor = int(input("Por favor, dame el valor sin impuestos: "))

# Calcula los impuestos
total, iva, income, municipal = singleton.calculate_impuestos(valor)

# Impuestos desglosados y el total al usuario
print(f"Impuesto VAT: {iva}")
print(f"Impuesto IIBB: {income}")
print(f"Impuesto Municipal: {municipal}")
print(f"Total de Impuestos: {total}")
