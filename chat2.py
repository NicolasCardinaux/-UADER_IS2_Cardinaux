import openai
import sys
import readline

# Configuración de la API de OpenAI
openai.api_key = 'tu_clave_api'

# Buffer para el modo de conversación
buffer_conversacion = []

def main():
    # Verificar si se proporcionó el argumento "--convers"
    modo_conversacion = "--convers" in sys.argv

    while True:
        try:
            # Aceptar la consulta del usuario
            consulta = input("You: ")

            # Verificar si la consulta tiene texto
            if consulta:
                # Agregar la consulta al buffer si estamos en modo de conversación
                if modo_conversacion:
                    buffer_conversacion.append(consulta)

                # Preparar la consulta para la API de chatGPT
                consulta_api = "\n".join(buffer_conversacion) if modo_conversacion else consulta

                # Invocar la API de chatGPT
                respuesta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": consulta_api},
                    ]
                )

                # Agregar la respuesta de chatGPT al buffer si estamos en modo de conversación
                if modo_conversacion:
                    buffer_conversacion.append(respuesta['choices'][0]['message']['content'])

                # Imprimir la respuesta
                print("chatGPT: ", respuesta['choices'][0]['message']['content'])
            else:
                print("Por favor, introduce una consulta.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
