'''Provea una clase ping que luego de creada al ser invocada con un método 
“execute(string)” realice 10 intentos de ping a la dirección IP contenida en “string”
(argumento pasado), la clase solo debe funcionar si la dirección IP provista comienza con “192.”.
Provea un método executefree(string) que haga lo mismo pero sin el control de dirección. 
Ahora provea una clase pingproxy cuyo método execute(string) si la dirección es “192.168.0.254” 
realice un ping a www.google.com usando el método executefree de ping y re-envie a execute de la
 clase ping en cualquier otro caso. (Modele la solución como un patrón proxy).'''
from abc import ABC, abstractmethod
import socket
class Ping(ABC):
    @abstractmethod
    def ejecute(self, ip):
        pass
class RealPing(Ping):
    #Solo si la ip comienza con 192. realiza la coneccion
    def ejecute(self, ip):
        if ip.startswith("192."):
            print("Probando RealPing.ejecute con IP:", ip)
            for _ in range(10):
                self.ejecutefree(ip)
    #Realiza la coneccion sin checkear la ip
    def ejecutefree(self, ip):
        print("Probando RealPing.ejecutefree con IP:", ip)
        try:
            socket.create_connection((ip, 80), timeout=5)
            print("coneccion establecida")
            return True
        except Exception as e:
            print("No se pudo conectar:", e)
            return False
class Proxy(Ping):
    def __init__(self, real_ping: RealPing) -> None:
        self._real_ping = real_ping
    def ejecute(self, ip):
        print("Probando Proxy.ejecute con IP:", ip)
        #Si ckeck_ip es True se conecta a la ip de google.com sin comprobar ip
        if self.check_ip(ip):
            print("IP es 192.168.0.254, intentando conectar con www.google.com")
            for _ in range(10):
                if self._real_ping.ejecutefree("172.217.167.196"):
                    print("Coneccion con www.google.com")
        else:
            print("IP no es 192.168.0.254, intentando conectar con la IP proporcionada")
            self._real_ping.ejecute(ip)
    def check_ip(self, ip):
        print("Verificando IP:", ip)
        if ip == "192.168.0.254":
            return True
        else:
            return False
#Ejecuta el metodo ejecute sin saber nada del objeto que lo implementa
def client_code(ping: Ping, ip):
    print("Ejecutando client_code con IP:", ip)
    ping.ejecute(ip)
if __name__ == "__main__":
    #Se instancia un RealPing
    real_ping = RealPing()
    #Se ejecuta client_code usando directamente el real_ping
    print("Probando RealPing directamente")
    client_code(real_ping, "192.168.0.1")
    print("")
    #Se instancia un proxy con el objeto real_ping
    proxy = Proxy(real_ping)
    #Se ejecuta client_code para generar la coneccion pero usando un proxy de intermediario
    print("Probando Proxy")
    client_code(proxy, "192.168.0.254")
