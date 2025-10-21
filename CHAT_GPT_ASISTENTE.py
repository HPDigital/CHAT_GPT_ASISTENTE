"""
CHAT_GPT_ASISTENTE
"""

#!/usr/bin/env python
# coding: utf-8

# In[23]:


from openai import OpenAI

def get_response(messages):
    client = OpenAI(api_key="YOUR_API_KEY_HERE")

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        response_format={ "type": "json_object" },
        messages=messages
    )

    return response

# Uso de la función con una conversación de ejemplo
messages = [
    {"role": "system", "content": "Eres un asistente experto en escritura de publicaciones cientificas de revision de la literatura y tu respuesta debe ser en formato JSON."},
    {"role": "user", "content": "Que publicaciones son las mas recientes contra el lavado de dinero con aprendisaje profundo"},
]

response = get_response(messages)
respuesta = response.choices[0].message.content

print(respuesta)


# In[ ]:






if __name__ == "__main__":
    pass
