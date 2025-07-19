def duplicati (stringa):
    s = stringa.lower()
    s = s.replace(".", "")

    parole = s.split()
    conteggio = {}
    
    for char in parole: 
        if char in conteggio: conteggio[char] += 1
        else: conteggio[char]=1

    for char, conteggio in conteggio.items(): lunghezza = len(char)
    print(f"{char} appare {conteggio} volte, e la sua lunghezza è di {lunghezza} caratteri")


stringa = input("Inserisci una frase: ")
duplicati(stringa)