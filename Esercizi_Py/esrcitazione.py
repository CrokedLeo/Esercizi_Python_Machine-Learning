alunni = {}

while True:
    nome = input("Inserisci il nome dell'alunno (oppure digita 'media' per terminare): ")

    if nome.lower() == "media":
        break

    voti_input = input(f"Inserisci i voti di {nome}, separati da una virgola: ")

    voti = [float(voto.strip()) for voto in voti_input.split(",")]

    alunni[nome] = voti

print("\nMedie degli alunni:")
for nome, voti in alunni.items():
    media = sum(voti) / len(voti)
    print(f"Nome: {nome}, Media: {media}")
