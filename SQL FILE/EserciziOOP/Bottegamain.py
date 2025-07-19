from bottega import BottegaMagica
from oggetti import OggettoMagico

bottega = BottegaMagica(oro_start=200)

def main():
    while True:
        print("Bottega delle Merdaviglie")
        print("1. Aggiungi oggetto")
        print("2. Mostra inventario")
        print("3. Vendi oggetto")
        print("4. Reso oggetto")
        print("5. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            categoria = input("Categoria (Pozioni/Artefatti/Pergamene): ").capitalize()
            nome = input("Nome oggetto: ")
            potere = input("Descrizione potere: ")
            prezzo = float(input("Prezzo (in oro): "))
            quantita = int(input("Quantità: "))
            oggetto = OggettoMagico(nome, potere, prezzo, quantita)
            bottega.aggiungi(categoria, oggetto)

        elif scelta == "2":
            bottega.mostra_inventario()

        elif scelta == "3":
            categoria = input("Categoria (Pozioni/Artefatti/Pergamene): ").capitalize()
            nome = input("Nome oggetto da vendere: ")
            quantita = int(input("Quantità da vendere: "))
            bottega.vendi(nome, categoria, quantita)

        elif scelta == "4":
            categoria = input("Categoria (Pozioni/Artefatti/Pergamene): ").capitalize()
            nome = input("Nome oggetto da rendere: ")
            quantita = int(input("Quantità da rendere: "))
            bottega.reso(nome, categoria, quantita)

        elif scelta == "5":
            print("Uscita dalla bottega. A presto!")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
