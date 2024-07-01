import openai
import os

# Configura tu API key de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Función para revisar el código
def revisar_codigo(codigo):
    respuesta = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=[
            {"role": "system", "content": "Eres un asistente útil que revisa código."},
            {"role": "user", "content": f"Revisa el siguiente código:\n\n{codigo}"}
        ],
        max_tokens=150
    )
    return respuesta.choices[0].message['content'].strip()

if __name__ == "__main__":
    codigo_ejemplo = """
    def sumar(a, b):
        return a + b
    """
    resultado = revisar_codigo(codigo_ejemplo)
    print("Revisión de código:", resultado)
