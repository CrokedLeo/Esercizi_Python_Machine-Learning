class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = True

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "In prestito"
        return f"{self.titolo} di {self.autore} - {stato}"

class Utente:
    def __init__(self, nome):
        self.nome = nome
        self.prestiti = []

    def prendi_in_prestito(self, libro):
        if libro.disponibile:
            libro.disponibile = False
            self.prestiti.append(libro)
            print(f"{self.nome} ha preso in prestito: {libro.titolo}")
        else:
            print(f"{libro.titolo} non è disponibile.")

    def restituisci_libro(self, libro):
        if libro in self.prestiti:
            libro.disponibile = True
            self.prestiti.remove(libro)
            print(f"{self.nome} ha restituito: {libro.titolo}")
        else:
            print(f"{self.nome} non ha questo libro in prestito.")

    def __str__(self):
        return f"{self.nome} - Prestiti: {[l.titolo for l in self.prestiti]}"

class Biblioteca:
    def __init__(self):
        self.libri = []
        self.utenti = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        print(f"Aggiunto libro: {libro.titolo} di {libro.autore}")

    def registra_utente(self, utente):
        self.utenti.append(utente)
        print(f"Registrato utente: {utente.nome}")

    def mostra_libri(self):
        print("\n--- LIBRI IN BIBLIOTECA ---")
        for libro in self.libri:
            print(libro)

    def mostra_utenti(self):
        print("\n--- UTENTI REGISTRATI ---")
        for utente in self.utenti:
            print(utente)




def interfaccia_biblioteca():
    biblioteca = Biblioteca()

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Aggiungi libro")
        print("2. Registra utente")
        print("3. Presta libro a utente")
        print("4. Restituisci libro")
        print("5. Mostra tutti i libri")
        print("6. Mostra tutti gli utenti")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            titolo = input("Titolo del libro: ")
            autore = input("Autore: ")
            biblioteca.aggiungi_libro(Libro(titolo, autore))

        elif scelta == "2":
            nome = input("Nome utente: ")
            biblioteca.registra_utente(Utente(nome))

        elif scelta == "3":
            nome = input("Nome utente: ")
            titolo = input("Titolo libro: ")
            utente = next((u for u in biblioteca.utenti if u.nome == nome), None)
            libro = next((l for l in biblioteca.libri if l.titolo == titolo), None)
            if utente and libro:
                utente.prendi_in_prestito(libro)
            else:
                print("Utente o libro non trovato.")

        elif scelta == "4":
            nome = input("Nome utente: ")
            titolo = input("Titolo libro: ")
            utente = next((u for u in biblioteca.utenti if u.nome == nome), None)
            if utente:
                libro = next((l for l in utente.prestiti if l.titolo == titolo), None)
                if libro:
                    utente.restituisci_libro(libro)
                else:
                    print("Libro non trovato nei prestiti dell'utente.")
            else:
                print("Utente non trovato.")

        elif scelta == "5":
            biblioteca.mostra_libri()

        elif scelta == "6":
            biblioteca.mostra_utenti()

        elif scelta == "0":
            print("Uscita dal sistema.")
            break

        else:
            print("Scelta non valida.")

# Avvio del programma:
if __name__ == "__main__":
    interfaccia_biblioteca()
