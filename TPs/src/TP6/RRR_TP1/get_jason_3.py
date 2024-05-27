"""
Extractor de token para acceso API Servicios Banco XXX (versión 1.1)

Este programa permite extraer la clave de acceso API para utilizar los servicios del
Banco XXX.

Copyright UADER- FCyT-IS2©2024 todos los derechos reservados

Uso: {path ejecutable}/getJason_3.pyc {path archivo JSON}/{nombre archivo JSON}.json [clave]
"""

import json
import sys
from abc import ABC, abstractmethod

# Definición de la interfaz KeyExtractor
class KeyExtractor(ABC):
    """Interfaz para la extracción de claves"""
    @abstractmethod
    def extract_key(self):
        """Método para extraer la clave"""
# Implementación de la interfaz KeyExtractor usando el patrón Singleton
class JsonKeyExtractor(KeyExtractor):
    """Clase para la extracción de claves de un archivo JSON"""
    _instance = None

    # Implementación del patrón Singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Inicialización de la instancia
    def __init__(self, json_file_path, json_key="token1"):
        self.json_file_path = json_file_path
        self.json_key = json_key

    # Método para extraer la clave del archivo JSON
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

# Punto de entrada del programa
def main():
    """Función principal"""
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        print("Uso:{path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json [clave]")
        sys.exit(0)
    if sys.argv[1] == "-v":
        print("versión 1.1")
        sys.exit(0)
    json_file_path = sys.argv[1]
    json_key = sys.argv[2] if len(sys.argv) > 2 else "token1"
    extractor = JsonKeyExtractor(json_file_path, json_key)
    print(extractor.extract_key())

if __name__ == "__main__":
    main()
