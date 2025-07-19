#import random as rd

from random import sample as s


def genera_numeri_casuali():
    numeri = s(range(1, 21), 5)  # 5 numeri tra 1 e 20
    with open("numeri_segreti.txt", "w") as file:
        for numero in numeri:
            file.write(str(numero) + "\n")

def leggi_numeri_file():
    with open("numeri_segreti.txt", "r") as file:
        return [int(line.strip()) for line in file]

def chiedi_numeri():
    numeri_utente = []
    print("Indovina i 5 numeri (tra 1 e 20):")
    while len(numeri_utente) < 5:
        try:
            numero = int(input(f"Numero {len(numeri_utente)+1}: "))
            if 1 <= numero <= 20:
                numeri_utente.append(numero)
            else:
                print("Inserisci numero tra 1 e 20.")
        except ValueError:
            print("Inserisci numero valido.")
    return numeri_utente

def controlla_vincita(numeri_segret, tentativi):
    indovinati = set(numeri_segret) & set(tentativi)
    if len(indovinati) >= 2:
        print(f"Hai vinto numeri: {list(indovinati)}")
    else:
        print(f"Hai perso indovinato solo: {list(indovinati)}")
        print(f"I numeri segreti erano: {numeri_segret}")

# principale
genera_numeri_casuali()
numeri_salvati = leggi_numeri_file()
numeri_utente = chiedi_numeri()
controlla_vincita(numeri_salvati, numeri_utente)
