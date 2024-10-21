'''Implemente una clase “factura” que tenga un importe correspondiente al total
de la factura pero de acuerdo a la condición impositiva del cliente (IVA
Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
condición'''
class Factura:
    def __init__(self, importe):
        self.importe = importe

    def calcular_impuesto(self):
        pass

class IvaResponsable(Factura):
    def calcular_impuesto(self):
        return self.importe * 0.21  #IVA del 21%

class IvaNoInscripto(Factura):
    def calcular_impuesto(self):
        return self.importe * 0.10  #IVA del 10%

class IvaExento(Factura):
    def calcular_impuesto(self):
        return 0  # No se aplica IVA

class FacturaFactory:
    def crear_factura(self, tipo, importe):
        if tipo == 'IVA Responsable':
            return IvaResponsable(importe)
        elif tipo == 'IVA No Inscripto':
            return IvaNoInscripto(importe)
        elif tipo == 'IVA Exento':
            return IvaExento(importe)
        else:
            raise ValueError("Tipo de factura no válido")

# Uso del Factory
factory = FacturaFactory()

# Interacción
tipo_factura = input("Ingrese su condición (IVA Responsable, IVA No Inscripto, IVA Exento): ")
importe_factura = float(input("Ingrese el importe de la factura: "))

# Crear factura
try:
    factura = factory.crear_factura(tipo_factura, importe_factura)
    impuesto = factura.calcular_impuesto()
    print("El impuesto a pagar es:", impuesto)
except ValueError as e:
    print(e)
