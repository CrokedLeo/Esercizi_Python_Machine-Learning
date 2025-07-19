# interfaccia
from gestione_studenti import *

def menu_principale():
    while True:
        print("\n--- GESTIONALE SCOLASTICO ---")
        print("1. Aggiungi studente")
        print("2. Aggiungi voto")
        print("3. Visualizza studenti")
        print("4. Modifica studente")
        print("5. Modifica voto")
        print("6. Elimina studente")
        print("7. Elimina voto")
        print("8. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            aggiungi_studente()
        elif scelta == "2":
            aggiungi_voto()
        elif scelta == "3":
            visualizza_studenti()
        elif scelta == "4":
            modifica_studente()
        elif scelta == "5":
            modifica_voto()
        elif scelta == "6":
            elimina_studente()
        elif scelta == "7":
            elimina_voto()
        elif scelta == "8":
            print("Uscita...")
            break
        else:
            print("Scelta non valida.")
