'''Asistente inteligente que proporciona respuesta a 
las preguntas que le des utilizando la api de 
openai'''

import argparse
import sys
import openai

# Configuramos la clave de la API de OpenAI
openai.api_key = ''

# Inicializamos una lista para almacenar el historial de consultas del usuario
query_history = []

# Configuramos el analizador de argumentos para aceptar un argumento
# de línea de comandos '--convers'
parser = argparse.ArgumentParser()
parser.add_argument('--convers', action='store_true', help='Activar el modo de conversación')
args = parser.parse_args()

# Verificamos si se ha proporcionado el argumento '--convers'
if args.convers:
    if '--convers' not in sys.argv:
        print("Argumento no reconocido. Usa '--convers' para activar el modo de conversación.")
        sys.exit()
    else:
        print("Modo de conversación activado.")

try:
    while True:
        userquery = input("Ingresa tu consulta ('x' para ver las consultas anteriores, o 'exit'): ")
        if userquery.strip().lower() == 'exit':
            print("Saliendo de la conversación. ¡Hasta luego!")
            break
        elif userquery.strip().lower() == 'x':
            for i, query in enumerate(query_history, 1):
                print(f"{i}: {query}")
            query_num = input("Selecciona la consulta que quieres editar o Enter para continuar: ")
            if query_num.isdigit() and int(query_num) <= len(query_history):
                userquery = input(f"Edita tu consulta ({query_history[int(query_num)-1]}): ")
                if userquery.strip():
                    query_history[int(query_num)-1] = userquery
                else:
                    print("La consulta no puede estar vacía.")
                    continue
        if userquery.strip():
            query_history.append(userquery)
        else:
            print("La consulta no puede estar vacía.")
            continue

        try:
            messages = [
                {
                    "role": "system",
                    "content": "Eres un ia inteligente que responde a cualquier consulta."
                }
            ]
            for query in query_history:
                messages.append({
                    "role": "user",
                    "content": query
                })
            message = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=1,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            try:
                response = message.choices[0].message['content']
                print(f"chatGPT: {response}")
                if args.convers:
                    query_history.append(response)
            except Exception as e:
                print(f"Hubo un error al invocar el API de chatGPT: {e}")
        except Exception as e:
            print(f"Hubo un error al tratar la consulta del usuario: {e}")
except Exception as e:
    print(f"Hubo un error al aceptar la consulta del usuario: {e}")
