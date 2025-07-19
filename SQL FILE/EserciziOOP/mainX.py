from fabbrica import Fabbrica

def main():
    fabbrica = Fabbrica()
    while True:
        print("\nMenu:")
        print("1. Aggiungi prodotto")
        print("2. Vendi prodotto")
        print("3. Resi prodotto")
        print("4. Visualizza inventario")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            fabbrica.aggiungi_prodotto()
        elif scelta == "2":
            fabbrica.vendi_prodotto()
        elif scelta == "3":
            fabbrica.resi_prodotto()
        elif scelta == "4":
            fabbrica.visualizza_inventario()
        elif scelta == "5":
            print("Uscita...")
            break
        else:
            print("Opzione non valida.")

if __name__ == "__main__":
    main()
