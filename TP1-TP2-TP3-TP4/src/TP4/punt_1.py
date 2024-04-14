'''1.	Provea una clase ping que luego de creada al ser invocada con un método “execute(string)”
realice 10 intentos de ping a la dirección IP contenida en “string” (argumento pasado),
la clase solo debe funcionar si la dirección IP provista comienza con “192.”. 
Provea un método executefree(string) que haga lo mismo pero sin el control de dirección. 
Ahora provea una clase pingproxy cuyo método execute(string) si la dirección es “192.168.0.254”
realice un ping a www.google.com usando el método executefree de ping y re-envie a execute
de la clase ping en cualquier otro caso. (Modele la solución como un patrón proxy).'''

import os

class Ping:
    def execute(self, ip):
        if ip.startswith("192."):
            for i in range(10):
                os.system(f"ping -c 1 {ip}")
        else:
            print("La dirección IP debe comenzar con '192.'")

    def executefree(self, ip):
        for i in range(10):
            os.system(f"ping -c 1 {ip}")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip):
        if ip == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip)

# Crear una instancia de la clase Ping
ping = Ping()

# Prueba el método execute con una dirección IP que comienza con "192."
print("Prueba 1: Método execute con IP válida")
ping.execute("192.168.2.1")

# Prueba el método execute con una dirección IP que no comienza con "192."
print("Prueba 2: Método execute con IP inválida")
ping.execute("10.0.0.1")

# Prueba el método executefree con cualquier dirección IP
print("Prueba 3: Método executefree")
ping.executefree("8.8.8.8")

# Crear una instancia de la clase PingProxy
ping_proxy = PingProxy()

# Prueba el método execute con la dirección IP "192.168.0.254"
print("Prueba 4: Método execute de PingProxy con IP 192.168.0.254")
ping_proxy.execute("192.168.0.254")

# Prueba el método execute con una dirección IP diferente a "192.168.0.254"
print("Prueba 5: Método execute de PingProxy con IP diferente a 192.168.0.254")
ping_proxy.execute("191.168.1.1")
