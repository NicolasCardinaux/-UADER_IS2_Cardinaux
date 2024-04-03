import openai


openai.api_key = ''

# Historial de consultas del usuario
query_history = []

try:
    while True:
        # Solicitar la consulta del usuario
        userquery = input("Por favor, ingresa tu consulta (o 'x' para ver las consultas anteriores, 'exit' para salir): ")

        # Verificar si el usuario quiere salir de la conversación
        if userquery.strip().lower() == 'exit':
            print("Saliendo de la conversación. ¡Hasta luego!")
            break

        # Verificar si el usuario quiere ver el historial de consultas
        elif userquery.strip().lower() == 'x':
            for i, query in enumerate(query_history, 1):
                print(f"{i}: {query}")
            query_num = input("Selecciona el número de la consulta que quieres editar o presiona Enter para continuar: ")
            if query_num.isdigit() and int(query_num) <= len(query_history):
                userquery = input(f"Edita tu consulta ({query_history[int(query_num)-1]}): ")
                if userquery.strip():
                    query_history[int(query_num)-1] = userquery  # Actualizar la consulta en el historial
                else:
                    print("La consulta no puede estar vacía.")
                    continue

        # Verificar si la consulta tiene texto
        if userquery.strip():
            query_history.append(userquery)  # Agregar la consulta al historial
            try:
                # Configuración del cliente de OpenAI
                message = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[
                        {
                            "role": "system",
                            "content": "Eres un asistente inteligente que puede responder a cualquier consulta."
                        },
                        {
                            "role": "user",
                            "content": userquery 
                        }
                    ],
                    temperature=1,
                    max_tokens=150,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                try:
                    # Invocar el API de chatGPT con la consulta del usuario
                    response = message.choices[0].message['content']
                    # Imprimir en pantalla el resultado obtenido como respuesta
                    print(f"chatGPT: {response}")
                except Exception as e:
                    print(f"Hubo un error al invocar el API de chatGPT: {e}")
            except Exception as e:
                print(f"Hubo un error al tratar la consulta del usuario: {e}")
        else:
            print("La consulta no puede estar vacía.")
except Exception as e:
    print(f"Hubo un error al aceptar la consulta del usuario: {e}")
