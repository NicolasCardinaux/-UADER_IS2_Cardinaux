'''
Asistente inteligente que utiliza la API de OpenAI para proporcionar respuestas 
a las preguntas de los usuarios.El programa permite interactuar 
en modo de conversación, almacenando el historial de consultas del usuario y 
ofreciendo la posibilidad de editar consultas anteriores. 
Además, utiliza el modelo de lenguaje GPT-3.5 de OpenAI 
para generar respuestas basadas en el contexto de la conversación
'''


# Importamos los módulos necesarios
import argparse  # Módulo para analizar argumentos de línea de comandos.
import sys  # Módulo para manejar la salida del programa.
import openai  # Biblioteca OpenAI para acceder a su API.

# Configuramos la clave de la API de OpenAI.
openai.api_key = ''

# Inicializamos una lista para almacenar el historial de consultas del usuario.
query_history = []

# Configuramos el analizador de argumentos para aceptar un argumento
# de línea de comandos '--convers'.
parser = argparse.ArgumentParser()
parser.add_argument('--convers', action='store_true', help='Activar el modo de conversación.')
args = parser.parse_args()

# Verificamos si se ha proporcionado el argumento '--convers'.
if args.convers:
    if '--convers' not in sys.argv:
        print("Argumento no reconocido. Usa '--convers' para activar el modo de conversación.")
        sys.exit()
    else:
        print("Modo de conversación activado.")

try:
    # Iniciamos el bucle principal de interacción con el usuario.
    while True:
        # Solicitamos al usuario que ingrese una consulta.
        userquery = input("Ingresa tu consulta ('x' para ver las consultas anteriores, o 'exit'): ")
        # Verificamos si el usuario desea salir de la conversación.
        if userquery.strip().lower() == 'exit':
            print("Saliendo de la conversación. ¡Hasta luego!")
            break
        # Verificamos si el usuario desea ver las consultas anteriores.
        if userquery.strip().lower() == 'x':
            # Mostramos las consultas anteriores enumeradas para que el usuario las seleccione.
            for i, query in enumerate(query_history, 1):
                print(f"{i}: {query}")
            # Solicitamos al usuario que seleccione una consulta para editarla.
            query_num = input("Selecciona la consulta que quieres editar o Enter para continuar: ")
            if query_num.isdigit() and int(query_num) <= len(query_history):
                # Editamos la consulta seleccionada si el usuario proporciona un texto válido.
                userquery = input(f"Edita tu consulta ({query_history[int(query_num)-1]}): ")
                if userquery.strip():
                    query_history[int(query_num)-1] = userquery
                else:
                    print("La consulta no puede estar vacía.")
                    continue
        # Verificamos si la consulta del usuario no está vacía.
        if userquery.strip():
            query_history.append(userquery)
        else:
            print("La consulta no puede estar vacía.")
            continue

        try:
            # Configuramos los mensajes para la API de chatGPT.
            messages = [
                {
                    "role": "system",
                    "content": "Eres un ia inteligente que responde a cualquier consulta."
                }
            ]
            # Agregamos las consultas del usuario al historial de mensajes.
            for query in query_history:
                messages.append({
                    "role": "user",
                    "content": query
                })
            # Realizamos la solicitud a la API de chatGPT para obtener la respuesta.
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
                # Obtenemos y mostramos la respuesta del modelo chatGPT.
                response = message.choices[0].message['content']
                print(f"chatGPT: {response}")
                # Agregamos la respuesta al historial si estamos en modo de conversación.
                if args.convers:
                    query_history.append(response)
            except AttributeError as e:
                print(f"Hubo un error al invocar el API de chatGPT: {e}")
        except AttributeError as e:
            print(f"Hubo un error al tratar la consulta del usuario: {e}")
except AttributeError as e:
    print(f"Hubo un error al aceptar la consulta del usuario: {e}")
