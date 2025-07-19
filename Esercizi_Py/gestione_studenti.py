# gestione_studenti
registro = "studenti.txt"

def carica_studenti():
    try:
        with open( registro, "r") as file:
            righe = file.readlines()
            return [eval(riga.strip()) for riga in righe]
    except FileNotFoundError:
        return []

def salva_studenti(studenti):
    with open(registro, "w") as file:
        for studente in studenti:
            file.write(f"{studente}\n")

def aggiungi_studente():
    nome = input("Nome studente: ")
    studenti = carica_studenti()
    studenti.append({"nome": nome, "voti": []})
    salva_studenti(studenti)
    print(f"Studente {nome} aggiunto.")

def aggiungi_voto():
    nome = input("Nome studente: ")
    voto = float(input("Inserisci voto: "))
    studenti = carica_studenti()
    for studente in studenti:
        if studente["nome"] == nome:
            studente["voti"].append(voto)
            salva_studenti(studenti)
            print("Voto aggiunto.")
            return
    print("Studente non trovato.")

def visualizza_studenti():
    studenti = carica_studenti()
    for studente in studenti:
        print(f"Nome: {studente['nome']}, Voti: {studente['voti']}")

def modifica_studente():
    vecchio_nome = input("Nome attuale dello studente: ")
    nuovo_nome = input("Nuovo nome: ")
    studenti = carica_studenti()
    for studente in studenti:
        if studente["nome"] == vecchio_nome:
            studente["nome"] = nuovo_nome
            salva_studenti(studenti)
            print("Nome modificato.")
            return
    print("Studente non trovato.")

def modifica_voto():
    nome = input("Nome studente: ")
    studenti = carica_studenti()
    for studente in studenti:
        if studente["nome"] == nome:
            print(f"Voti attuali: {studente['voti']}")
            idx = int(input("Indice del voto da modificare: "))
            nuovo_voto = float(input("Nuovo voto: "))
            studente["voti"][idx] = nuovo_voto
            salva_studenti(studenti)
            print("Voto modificato.")
            return
    print("Studente non trovato.")

def elimina_studente():
    nome = input("Nome studente da eliminare: ")
    studenti = carica_studenti()
    studenti = [s for s in studenti if s["nome"] != nome]
    salva_studenti(studenti)
    print("Studente eliminato.")

def elimina_voto():
    nome = input("Nome studente: ")
    studenti = carica_studenti()
    for studente in studenti:
        if studente["nome"] == nome:
            print(f"Voti: {studente['voti']}")
            
            idx = int(input("Indice del voto da eliminare: "))
            del studente["voti"][idx]
            salva_studenti(studenti)
            print("Voto eliminato.")
            return
    print("Studente non trovato.")
