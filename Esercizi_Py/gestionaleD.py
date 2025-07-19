def leggi_file():
    try:
        with open("registro.txt", "r") as file:
            registro = {}
            rows = file.read().split("\n")
            print(rows)
            voti = []

            for row in rows:
                if not row.strip():  # salta righe vuote
                    continue

                nome, voti_str = row.split(":")
                voti_str = voti_str.strip("[]").strip()

                if voti_str:  # solo se ci sono voti
                    voti = [float(v.strip()) for v in voti_str.split(",")]
                else:
                    voti = []

                registro[nome] = voti
    except:
        print("Errore in lettura del file\n")
        
    return registro

def scrivi_registro(registro):
    try:
        with open("registro.txt", "w") as file:
            for key, value in registro.items():
                file.write(f"{key}:{value}\n")
    except:
        print("Errore in scrittura del file\n")


    

def gestionale_scolastico():
    while True:
        opzione = input('Cosa vuoi fare?\n1: Inserire alunno\n2: Inserire voto\n3: Elimina voto\n4: Esci\n')
        if opzione == '1':
            inserisci_alunno()
        elif opzione == '2':
            inserisci_voto()
        elif opzione == '3':
            elimina_voto()
        elif opzione == '4':
            print("Grazie per aver usato il gestionale scolastico")
            break
        else:
            print("Valore non valido\n")


def inserisci_alunno():
    registro = leggi_file()
    nome_alunno = input("Come si chiama l'alunno?\n")

    if nome_alunno not in registro:
        try:
            with open("registro.txt", "a") as file:
                file.write("\n" + nome_alunno + ":" + "[]")
            print("Alunno inserito correttamente\n")
        except:
            print("Errore nella scrittura del file\n")
    else:
        print("L'alunno esiste giÃ\n")
    

def inserisci_voto(): 
    registro = leggi_file()

    nome_alunno = input('A quale alunno vuoi inserire il voto?\n')
    if nome_alunno in registro:
        voto = input("Quale voto vuoi aggiungere?\n")
        registro[nome_alunno].append(float(voto))
        #print(type(registro[nome_alunno]))
        scrivi_registro(registro)
        print("Voto aggiunto correttamente\n")
    else:
        print("Alunno non trovato\n")




def elimina_voto():
    registro = leggi_file()

    nome_alunno = input('A quale alunno vuoi cancellare un voto?\n')
    if nome_alunno in registro:
        voto = input("Quale voto vuoi eliminare?\n")
        #print(registro[nome_alunno])
        if float(voto) in registro[nome_alunno]:
            registro[nome_alunno].remove(float(voto))
            scrivi_registro(registro)
            print("Voto eliminato correttamente\n")
        else:
            print("Voto non presente\n")
    else:
        print("Alunno non trovato\n")
