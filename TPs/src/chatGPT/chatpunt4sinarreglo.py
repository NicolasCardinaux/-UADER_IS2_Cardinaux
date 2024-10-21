# Importamos las bibliotecas necesarias
import openai
import argparse
import sys

# Configuramos la clave de la API de OpenAI
# Esta clave se utiliza para autenticar nuestras solicitudes a la API de OpenAI
openai.api_key = ''

# Inicializamos una lista para almacenar el historial de consultas del usuario
# Esta lista actúa como un buffer que mantiene un registro de todas las consultas y respuestas en la conversación
query_history = []

# Configuramos el analizador de argumentos para aceptar un argumento de línea de comandos '--convers'
# Este argumento activará el modo de conversación cuando se ejecute el script
parser = argparse.ArgumentParser()
parser.add_argument('--convers', action='store_true', help='Activar el modo de conversación')
args = parser.parse_args()

# Verificamos si se ha proporcionado el argumento '--convers'
# Si se ha proporcionado un argumento, pero no es '--convers', mostramos un mensaje de error y salimos
# Si se ha proporcionado el argumento '--convers', activamos el modo de conversación
if args.convers:
    if '--convers' not in sys.argv:
        print("Argumento no reconocido. Por favor, usa '--convers' para activar el modo de conversación.")
        sys.exit()
    else:
        print("Modo de conversación activado.")

# Iniciamos un bucle para interactuar con el usuario
# Este bucle continuará hasta que el usuario ingrese 'exit' para salir de la conversación
try:
    while True:
        # Solicitamos una consulta al usuario.
        # El usuario puede ingresar una consulta, 'x' para ver y editar las consultas anteriores, o 'exit' para salir de la conversación
        userquery = input("Por favor, ingresa tu consulta (o 'x' para ver las consultas anteriores, 'exit' para salir): ")
        
        # Si el usuario ingresa 'exit', terminamos la conversación
        if userquery.strip().lower() == 'exit':
            print("Saliendo de la conversación. ¡Hasta luego!")
            break
        
        # Si el usuario ingresa 'x', mostramos el historial de consultas y permitimos al usuario editar una consulta anterior
        elif userquery.strip().lower() == 'x':
            for i, query in enumerate(query_history, 1):
                print(f"{i}: {query}")
            query_num = input("Selecciona el número de la consulta que quieres editar o presiona Enter para continuar: ")
            if query_num.isdigit() and int(query_num) <= len(query_history):
                userquery = input(f"Edita tu consulta ({query_history[int(query_num)-1]}): ")
                if userquery.strip():
                    query_history[int(query_num)-1] = userquery
                else:
                    print("La consulta no puede estar vacía.")
                    continue
        
        # Si el usuario ingresa una consulta no vacía, la agregamos al historial de consultas
        if userquery.strip():
            query_history.append(userquery)
        else:
            print("La consulta no puede estar vacía.")
            continue

        # Intentamos interactuar con chatGPT utilizando la consulta del usuario
        try:
            # Preparamos los mensajes para enviar a chatGPT
            # Cada mensaje consta de un rol (sistema o usuario) y un contenido (la consulta o respuesta)
            messages = [
                {
                    "role": "system",
                    "content": "Eres un asistente inteligente que puede responder a cualquier consulta."
                }
            ]
            # Agregamos todas las consultas y respuestas anteriores al mensaje
            for query in query_history:
                messages.append({
                    "role": "user",
                    "content": query
                })
            
            # Creamos el objeto ChatCompletion con los mensajes preparados
            # Este objeto se enviará a la API de OpenAI para obtener una respuesta de chatGPT
            message = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=1,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
                
            # Intentamos obtener la respuesta de chatGPT
            try:
                response = message.choices[0].message['content']
                print(f"chatGPT: {response}")
                # Si estamos en modo de conversación, agregamos la respuesta de chatGPT al historial de consultas
                if args.convers:
                    query_history.append(response)
            except Exception as e:
                print(f"Hubo un error al invocar el API de chatGPT: {e}")
        except Exception as e:
            print(f"Hubo un error al tratar la consulta del usuario: {e}")
except Exception as e:
    print(f"Hubo un error al aceptar la consulta del usuario: {e}")
