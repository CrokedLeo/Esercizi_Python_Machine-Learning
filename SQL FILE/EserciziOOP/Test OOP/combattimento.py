import random

def scontro_round(esercito_giocatore, esercito_ia):
    # Unisci i due eserciti in una lista per il round
    # Alterna gli attacchi o fai tutti i giocatori e poi tutti gli IA, a seconda della logica voluta
    # Qui alterniamo casualmente l'ordine di attacco
    combattenti = esercito_giocatore + esercito_ia
    random.shuffle(combattenti)

    # Per tenere traccia dei soldati morti da rimuovere
    morti_gio = []
    morti_ia = []

    for soldato in combattenti:
        # Controlla se il soldato è ancora vivo (non rimosso)
        if soldato in esercito_giocatore:
            avversari = esercito_ia
        else:
            avversari = esercito_giocatore

        if not avversari:
            # Nessun avversario rimasto, round termina
            break

        # Scegli avversario casuale
        bersaglio = random.choice(avversari)

        # Il soldato attacca il bersaglio
        soldato.attacca(bersaglio)

        # Controlla se il bersaglio è morto (vita <= 0)
        if bersaglio._vita <= 0:
            if bersaglio in esercito_giocatore:
                morti_gio.append(bersaglio)
            else:
                morti_ia.append(bersaglio)

    # Rimuovi i soldati morti dagli eserciti
    for morto in morti_gio:
        esercito_giocatore.remove(morto)
    for morto in morti_ia:
        esercito_ia.remove(morto)
