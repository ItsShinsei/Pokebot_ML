from google import generativeai
import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
generativeai.configure(api_key=api_key)

model = generativeai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        types = ', '.join([t['type']['name'] for t in data['types']])
        height = data['height']
        weight = data['weight']
        return f"{name.capitalize()} adalah Pokémon bertipe {types}. Tinggi: {height}, Berat: {weight}."
    else:
        return None

def chat_inference(prompt):
    words = prompt.lower().split()
    for word in words:
        info = get_pokemon_info(word)
        if info:
            return info
    pokemon_keywords = [
        "pokemon", "evolution", "trainer", "gym", "pokeball", "ash", "pikachu", "charizard", "bulbasaur", "squirtle"
    ]
    if any(keyword in prompt.lower() for keyword in pokemon_keywords):
        response = chat.send_message(prompt)
        return response.text
    return "Maaf, saya hanya dapat menjawab pertanyaan seputar dunia Pokémon."


# from google import generativeai
# import os
# import requests
# from dotenv import load_dotenv
# load_dotenv()

# api_key = os.getenv("API_KEY")
# client  = generativeai.Client(api_key=api_key)
# chat  = client.chats.create(model="gemini-2.0-flash")

# def get_pokemon_info(name):
#     url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         types = ', '.join([t['type']['name'] for t in data['types']])
#         height = data['height']
#         weight = data['weight']
#         return f"{name.capitalize()} adalah Pokémon bertipe {types}. Tinggi: {height}, Berat: {weight}."
#     else:
#         return None

# def chat_inference(prompt):
   
#     words = prompt.lower().split()
#     for word in words:
#         info = get_pokemon_info(word)
#         if info:
#             return info
   
#     pokemon_keywords = [
#         "pokemon", "evolution", "trainer", "gym", "pokeball", "ash", "pikachu", "charizard", "bulbasaur", "squirtle"
#     ]
#     if any(keyword in prompt.lower() for keyword in pokemon_keywords):
#         response = chat.send_message(prompt)
#         return response.text
   
#     return "Maaf, saya hanya dapat menjawab pertanyaan seputar dunia Pokémon."
