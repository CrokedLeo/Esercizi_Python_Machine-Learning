
# definisco le clessi
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return f"'{self.titolo}' di {self.autore}, {self.pagine} pagine"


class Biblioteca:
    def __init__(self):
        self.libri = []  # lista per contenere i libri

    def aggiungi_libro(self, titolo, autore, pagine):
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)
        print(f"Libro aggiunto: {libro.descrizione()}")

    def stampa_libri(self):
        if not self.libri:
            print("Nessun libro nella biblioteca.")
        else:
            print("\nLibri nella biblioteca:")
            for i, libro in enumerate(self.libri, 1):
                print(f"{i}. {libro.descrizione()}")


# main
biblioteca = Biblioteca()

while True:
    print("\n1. Aggiungi un libro\n2. Mostra tutti i libri\n3. Esci")
    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        pagine = input("Numero di pagine: ")
        if pagine.isdigit():
            biblioteca.aggiungi_libro(titolo, autore, int(pagine))
        else:
            print("Inserisci un numero valido per le pagine.")
    elif scelta == "2":
        biblioteca.stampa_libri()
    elif scelta == "3":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida.")
