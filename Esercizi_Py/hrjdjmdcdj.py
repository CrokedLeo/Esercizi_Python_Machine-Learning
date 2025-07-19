try:
    with open("lorem.txt", "r") as file:
        content = file.read()

    rows = content.split("\n")
    punteggiatura = '.,;!?\n'

    content = "".join([char for char in content if char not in punteggiatura])

    count_characters = 0

    for ind in range(len(rows)):
        count_characters += len(rows[ind])

    list_words = content.split(" ")

    print(f"Nel testo ci sono {count_characters} caratteri, {len(list_words)} parole e {len(rows)} righe")
except:
    print("Errore: probabilmente il file non è stato trovato")