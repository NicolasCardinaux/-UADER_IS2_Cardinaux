import os

# Clase Director
class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPlane(self):
        plane = Plane()

        # Construir el cuerpo del avión
        body = self.__builder.getBody()
        plane.setBody(body)

        # Construir las turbinas
        for _ in range(2):
            engine = self.__builder.getEngine()
            plane.attachEngine(engine)

        # Construir las alas
        for _ in range(2):
            wing = self.__builder.getWing()
            plane.attachWing(wing)

        # Construir el tren de aterrizaje
        landing_gear = self.__builder.getLandingGear()
        plane.setLandingGear(landing_gear)

        return plane

# Clase Avión
class Plane:
    def __init__(self):
        self.__engines = []
        self.__wings = []
        self.__body = None
        self.__landing_gear = None

    def setBody(self, body):
        self.__body = body

    def attachEngine(self, engine):
        self.__engines.append(engine)

    def attachWing(self, wing):
        self.__wings.append(wing)

    def setLandingGear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print("Cuerpo del avión: %s" % (self.__body.shape))
        print("Número de turbinas: %d" % len(self.__engines))
        print("Número de alas: %d" % len(self.__wings))
        print("Tipo de tren de aterrizaje: %s" % (self.__landing_gear.type))

# Builder genérico
class Builder:
    def getBody(self):
        pass
    def getEngine(self):
        pass
    def getWing(self):
        pass
    def getLandingGear(self):
        pass
# Builder específico para aviones
class AirplaneBuilder(Builder):
    def getBody(self):
        body = Body()
        body.shape = "Jet"
        return body
    def getEngine(self):
        engine = Engine()
        engine.type = "Turbina de avión"
        return engine
    def getWing(self):
        wing = Wing()
        wing.type = "Ala de avión"
        return wing
    def getLandingGear(self):
        landing_gear = LandingGear()
        landing_gear.type = "Tren de aterrizaje de avión"
        return landing_gear

# Clase genérica para partes de un avión
class Body:
    shape = None

class Engine:
    type = None

class Wing:
    type = None

class LandingGear:
    type = None

# Función principal
def main():
    airplaneBuilder = AirplaneBuilder()
    director = Director()
    director.setBuilder(airplaneBuilder)
    airplane = director.getPlane()
    airplane.specification()

if __name__ == "__main__":
    os.system("clear")
    print("Ejemplo de un patrón Builder aplicado a la construcción de un avión\n")
    main()


