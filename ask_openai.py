import openai

openai.api_key = 'sk-Your-OpenAI-API-Key'

def ask_chatGPT(content: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=1000,
        temperature=0.5,
        messages=content
    )
    return response.choices[0].message.content
