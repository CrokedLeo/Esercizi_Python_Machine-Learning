#input
input_utente = input("Inserisci parole separate da spazi o virgole: ")
#divide le parole e rimuove spazi extra
numeri = [parola.strip() for parola in input_utente.replace(",", " ").split()]
#calcola la lunghezza
lunghezze = [len(parola) for parola in numeri]

print("lista lunghezze:", lunghezze)
