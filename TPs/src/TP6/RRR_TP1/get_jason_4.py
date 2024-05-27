"""
Extractor de token para acceso API Servicios Banco XXX (versión 1.2)
Este programa permite extraer la clave de acceso API para utilizar los servicios del Banco XXX.
Copyright UADER- FCyT-IS2©2024 todos los derechos reservados
Uso: {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json [clave]
"""
import json
import sys
from abc import ABC, abstractmethod
class KeyExtractor(ABC):
    """Interfaz para la extracción de claves"""
    @abstractmethod
    def extract_key(self):
        """Método para extraer la clave"""
class JsonKeyExtractor(KeyExtractor):
    """Clase para la extracción de claves de un archivo JSON"""
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, json_file_path, json_key="token1"):
        self.json_file_path = json_file_path
        self.json_key = json_key
    def extract_key(self):
        """Extrae la clave del archivo JSON"""
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as myfile:
                data = myfile.read()
        except FileNotFoundError:
            print("Error: El archivo JSON especificado no se encuentra.")
            sys.exit(1)
        try:
            obj = json.loads(data)
        except json.JSONDecodeError:
            print("Error: El archivo JSON tiene un formato incorrecto.")
            sys.exit(1)
        try:
            return str(obj[self.json_key])
        except KeyError:
            print(f"Error: La clave '{self.json_key}' no se encontró en el archivo JSON.")
            sys.exit(1)
class PaymentRequest:
    """Clase para representar un pedido de pago"""
    def __init__(self, order_number, amount):
        self.order_number = order_number
        self.amount = amount
class PaymentProcessor:
    """Clase para procesar los pagos utilizando el patrón de diseño 'cadena de comando'"""
    def __init__(self, json_file_path):
        self.extractor1 = JsonKeyExtractor(json_file_path, "token1")
        self.extractor2 = JsonKeyExtractor(json_file_path, "token2")
        self.accounts = {
            "token1": {"balance": 1000, "key_extractor": self.extractor1},
            "token2": {"balance": 2000, "key_extractor": self.extractor2}
        }
        self.payments = []
        self.errors = []
    def process_payment(self, payment_request):
        """Procesa un pedido de pago"""
        for account_name in ["token1", "token2"]:
            if self.accounts[account_name]["balance"] >= payment_request.amount:
                token = self.accounts[account_name]["key_extractor"].extract_key()
                self.payments.append((payment_request.order_number, account_name, payment_request.amount))
                self.accounts[account_name]["balance"] -= payment_request.amount
                return
        self.errors.append(f"Error: Ninguna cuenta tiene saldo suficiente para el pedido {payment_request.order_number}.")
    def list_payments(self):
        """Lista todos los pagos realizados en orden cronológico"""
        for payment in self.payments:
            print(f"Pedido: {payment[0]}, Token: {payment[1]}, Monto: {payment[2]}")
        for error in self.errors:
            print(error)
def main():
    """Función principal"""
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        print("Uso:{path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json [clave]")
        sys.exit(0)
    if sys.argv[1] == "-v":
        print("versión 1.2")
        sys.exit(0)
    json_file_path = sys.argv[1]
    # Verificación del archivo JSON
    if not json_file_path.endswith('.json'):
        print("Error: El archivo especificado no tiene una extensión JSON.")
        sys.exit(1)
    payment_processor = PaymentProcessor(json_file_path)
    # Ejemplo de procesamiento de pagos
    for order_number in range(1, 10):
        payment_request = PaymentRequest(order_number, 500)
        payment_processor.process_payment(payment_request)
    payment_processor.list_payments()
    # Verificar saldo al finalizar
    any_account_has_balance = any(account["balance"] > 0 for account in payment_processor.accounts.values())
    if not any_account_has_balance:
        print("Ninguna cuenta tiene saldo suficiente para procesar más pagos.")
if __name__ == "__main__":
    main()
