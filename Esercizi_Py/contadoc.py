def analizza_file(nome_file):
    try:                           # assiura che vengano letti tutti i caratteri 
        with open(nome_file, 'r', encoding='utf-8') as file:
            testo = file.read()
            
            righe = testo.splitlines()                 # Lista delle righe
            parole = testo.split()                     # Lista delle parole (divise da spazi)
            caratteri = len(testo)                     # Tutti i caratteri, inclusi spazi e a capo

            print(f"Numero di righe: {len(righe)}")
            print(f"Numero di parole: {len(parole)}")
            print(f"Numero di caratteri: {caratteri}")
    except FileNotFoundError:
        print("Il file non è stato trovato.")
    except Exception as e:
        print(f"Errore: {e}")

# Esegui il programma
analizza_file("lipsum.txt")
