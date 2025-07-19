from inserimento import inserisci_libro
from ricerca import ricerca_libri
from prestiti import effettua_prestito, restituisci_libro

def menu():
    while True:
        print("\n--- Gestione Biblioteca ---")
        print("1. Inserisci un nuovo libro")
        print("2. Cerca libri")
        print("3. Effettua prestito")
        print("4. Restituisci libro")
        print("5. Esci")

        scelta = input("Scegli un'opzione: ").strip()

        if scelta == "1":
            inserisci_libro()
        elif scelta == "2":
            ricerca_libri()
        elif scelta == "3":
            effettua_prestito()
        elif scelta == "4":
            restituisci_libro()
        elif scelta == "5":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    menu()
