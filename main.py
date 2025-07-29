from google import genai
import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
client  = genai.Client(api_key=api_key)
chat  = client.chats.create(model="gemini-2.0-flash")

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
    # List of all Pokémon names (for demo, you can load from PokeAPI or a static list)
    # For now, let's check using the API for each word (as before)

    words = prompt.lower().split()
    for word in words:
        info = get_pokemon_info(word)
        if info:
            return info
    # If the prompt contains the word "pokemon" or other related keywords, use Gemini
    pokemon_keywords = [
        "pokemon", "evolution", "trainer", "gym", "pokeball", "ash", "pikachu", "charizard", "bulbasaur", "squirtle"
    ]
    if any(keyword in prompt.lower() for keyword in pokemon_keywords):
        response = chat.send_message(prompt)
        return response.text
    # If not related to Pokémon at all
    return "Maaf, saya hanya dapat menjawab pertanyaan seputar dunia Pokémon."
