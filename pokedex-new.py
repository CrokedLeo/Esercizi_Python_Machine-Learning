import requests
import json
import random
import time

def carica_pokedex():
    try:
        with open("pokedex.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salva_pokedex(pokemon):
    pokedex = carica_pokedex()
    pokedex[str(pokemon["id"])] = pokemon
    with open("pokedex.json", "w") as f:
        json.dump(pokedex, f, indent=4)

def ricerca_pokemon(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)
    dictResponse = response.json()
    nome = dictResponse["name"]
    altezza = dictResponse["height"]
    peso = dictResponse["weight"]
    esperienza_base = dictResponse['base_experience']
    abilities = [a['ability']['name'] for a in dictResponse['abilities']]
    pokemon = {
        "id": id,
        "nome": nome,
        "altezza": altezza,
        "peso": peso,
        "esperienza": esperienza_base,
        "abilita": abilities
    }

    print(f"E' appparso un {nome.capitalize()} selvatico.")
    return pokemon



def cattura_pokemon(pokemon, prob):
    if random.random() < prob:
        print("Hai catturato il Pokémon!")
        salva_pokedex(pokemon)
        stampa_pokemon(pokemon)
    else:
        print("Cattura fallita del Pokémon.")

def controlla_pokedex(pokemon_da_inserire, prob):
    pokedex = carica_pokedex()
    id_str = str(pokemon_da_inserire["id"])
    if id_str in pokedex:
        print(f"{pokemon_da_inserire['nome'].capitalize()} è già presente nel Pokédex.")
    else:
        cattura_pokemon(pokemon_da_inserire, prob)

def stampa_pokemon(pokemon):
    print("\nDettagli del Pokémon catturato:")
    print(f"ID: {pokemon['id']}")
    print(f"Nome: {pokemon['nome'].capitalize()}")
    print(f"Altezza: {pokemon['altezza']}")
    print(f"Peso: {pokemon['peso']}")
    print(f"Esperienza base: {pokemon['esperienza']}")
    print(f"Abilità: {', '.join(pokemon['abilita'])}")
    print()

def main():
    print("Benvuto nella regione di Kanto\n")
    while True:
        numero = random.randint(1, 1000)
        print("Stai camminando....\nATTENZIONE! Hai incontrato un nuovo pokemon selvaggio...")
        time.sleep(2)
        try:
            pokemon = ricerca_pokemon(numero)
            scelta2 = input("Quale pokeball vuoi usare?\n(1 per pokeball 2 per masterball): ")
            if scelta2 == "1":
                controlla_pokedex(pokemon, 0.8)
            elif scelta2 == "2":
                if random.random() < 0.3:
                    print("Lancio masterball riuscito!")
                    prob = 1.1
                else:
                    print("Lancio masterball fallito...\nLancio pokeball")
                    prob = 0.8                    
                controlla_pokedex(pokemon, prob)
            else:
                print("Scelta non valida.\n!!!Il pokemon è fuggito!!!")
        except Exception as e:
            print(f"Errore durante la ricerca del Pokémon con ID {numero}: {e}")
        
        while True:
            scelta3 = input("Vuoi continuare a cercare pokemon? (si/no): ").lower()
            if scelta3 == "no":
                print("Arrivederci!")
                exit()
            elif scelta3 == "si":
                break
            else:
                print("Errore inserimento dati. Inserisci 'si' o 'no'.")

main()