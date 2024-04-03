import openai
# Establecer la clave de API de OpenAI
openai.api_key = ''
# Solicitar la consulta del usuario
userquery = input("Ingresa tu consulta: ")
# Verificar si la consulta tiene texto
if userquery.strip():
    print(f"You: {userquery}")
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
                "content": userquery  # Aquí va la consulta del usuario
            }
        ],
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Invocar el API de chatGPT con la consulta del usuario
    response = message.choices[0].message['content']
    # Imprimir en pantalla el resultado obtenido como respuesta
    print(f"chatGPT: {response}")
else:
    print("La consulta no puede estar vacía.")
