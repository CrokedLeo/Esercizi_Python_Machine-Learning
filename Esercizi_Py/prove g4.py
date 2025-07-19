def duplicates(stringa:str):
    s = "".join([char for char in stringa if char.isalnum() or char == " "]) # eliminazione caratteri speciali
    s = s.lower()
    words = s.split(" ") # lista delle parole
    rep = {} 
    verbose = True

    for i in words: # algoritmo di ricerca e memorizzazione
        rep[i] = rep.get(i, 0) + 1

    for i,j in rep.items(): # ciclo di stampa
        if j>1: print(f"Parola: {i}. Ripetizioni: {j}. Lunghezza: {len(i)}")
        