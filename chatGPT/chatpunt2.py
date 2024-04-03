import openai


openai.api_key = ''

try:
    # Solicitar la consulta del usuario
    userquery = input("Por favor, ingresa tu consulta: ")

    # Verificar si la consulta tiene texto
    if userquery.strip():
        print(f"You: {userquery}")
        try:
          
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
