import json
import sys

# Comprueba si se proporcionó una clave como argumento. Si no, usa "token1" como valor predeterminado.
jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"

try:
    # Intenta abrir y leer el archivo JSON.
    with open(sys.argv[1], 'r') as myfile:
        data = myfile.read()
except FileNotFoundError:
    print("Error: El archivo JSON especificado no se encuentra.")
    sys.exit(1)

try:
    # Intenta cargar el contenido del archivo en un objeto JSON.
    obj = json.loads(data)
except json.JSONDecodeError:
    print("Error: El archivo JSON tiene un formato incorrecto.")
    sys.exit(1)

try:
    # Intenta imprimir el valor asociado con la clave especificada.
    print(str(obj[jsonkey]))
except KeyError:
    print(f"Error: La clave '{jsonkey}' no se encontró en el archivo JSON.")
    sys.exit(1)

