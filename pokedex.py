'''Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in
caso non fosse presente vi permetterà di catturarlo salvando il
numero identificativo, nome, abilità, xp(punti esperienza),peso
e altezza.
(Sul sistema API sono presenti poco più di 1000 pokemon)'''

import requests
import json
import random

FILE_POKEDEX = 'pokedex.json'
URL_POKEAPI = 'https://pokeapi.co/api/v2/pokemon/'

# Carica il pokedex dal file JSON
def carica_pokedex():
    try:
        with open(FILE_POKEDEX, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Salva il pokedex nel file JSON
def salva_pokedex(pokedex):
    with open(FILE_POKEDEX, 'w') as file:
        json.dump(pokedex, file, indent=4)

# Controlla se un Pokémon è già nel Pokédex (per ID o nome)
def pokemon_presente(pokedex, id_pokemon=None, nome_pokemon=None):
    if id_pokemon and str(id_pokemon) in pokedex:
        return True
    if nome_pokemon:
        for dati in pokedex.values():
            if dati['nome'].lower() == nome_pokemon.lower():
                return True
    return False

# Ottiene i dati del Pokémon da PokeAPI
def ottieni_dati_pokemon(id_pokemon):
    risposta = requests.get(f"{URL_POKEAPI}{id_pokemon}")
    if risposta.status_code == 200:
        dati = risposta.json()
        return {
            "id": dati["id"],
            "nome": dati["name"],
            "abilità": [a["ability"]["name"] for a in dati["abilities"]],
            "xp": dati["base_experience"],
            "peso": dati["weight"],
            "altezza": dati["height"]
        }
    return None

# Simula un incontro casuale con un Pokémon
def incontra_pokemon(pokedex):
    id_pokemon = random.randint(1, 1000)
    if pokemon_presente(pokedex, id_pokemon):
        print(f"\nHai già catturato il Pokémon n. {id_pokemon} ({pokedex[str(id_pokemon)]['nome'].capitalize()})")
    else:
        pokemon = ottieni_dati_pokemon(id_pokemon)
        if pokemon:
            print("\nHai incontrato un nuovo Pokémon!")
            print(f"ID: {pokemon['id']}")
            print(f"Nome: {pokemon['nome'].capitalize()}")
            print(f"Abilità: {', '.join(pokemon['abilità'])}")
            print(f"Esperienza: {pokemon['xp']}")
            print(f"Peso: {pokemon['peso']}")
            print(f"Altezza: {pokemon['altezza']}")
            scelta = input("Vuoi catturarlo? (s/n): ").strip().lower()
            if scelta == 's':
                pokedex[str(id_pokemon)] = pokemon
                salva_pokedex(pokedex)
                print(f"{pokemon['nome'].capitalize()} è stato aggiunto al Pokédex.")
            else:
                print("Hai deciso di non catturarlo.")
        else:
            print("Errore nel recupero dei dati del Pokémon.")

# Mostra tutti i Pokémon catturati nel pokedex
def mostra_pokedex(pokedex):
    if not pokedex:
        print("\nIl Pokédex è vuoto.")
        return
    print(f"\nHai catturato {len(pokedex)} Pokémon:")
    for p in sorted(pokedex.values(), key=lambda x: x['id']):
        print(f"#{p['id']:>4} | {p['nome'].capitalize():<15} | XP: {p['xp']:<3} | Altezza: {p['altezza']} | Peso: {p['peso']}")
        print(f"     Abilità: {', '.join(p['abilità'])}")

# Menu principale
def menu_principale():
    print("Benvenuto nel tuo Pokédex personale")
    pokedex = carica_pokedex()

    while True:
        print("\n--- Menu ---")
        print("1. Cerca un nuovo Pokémon")
        print("2. Visualizza Pokémon catturati")
        print("3. Esci")
        scelta = input("Scegli un'opzione (1-3): ").strip()

        if scelta == '1':
            incontra_pokemon(pokedex)
        elif scelta == '2':
            mostra_pokedex(pokedex)
        elif scelta == '3':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    menu_principale()
