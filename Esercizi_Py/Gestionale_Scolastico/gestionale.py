import database_manager

class GestionaleScolastico:
    def __init__(self, db_manager):
        self.db = db_manager

    def mostra_menu(self):
        print("""
<> Gestionale Scolastico <>
1. Inserisci studente
2. Inserisci voto studente
3. Visualizza studenti e medie
4. Modifica studente
5. Elimina studente
6. Esci
""")

    def avvia(self):
        while True:
            self.mostra_menu()
            scelta = input("Scelta: ")
            if scelta == "1":
                self.inserisci()
            elif scelta == "2":
                self.inserisci_voto()
            elif scelta == "3":
                self.visualizza()
            elif scelta == "4":
                self.modifica()
            elif scelta == "5":
                self.elimina()
            elif scelta == "6":
                print("Uscita in corso...")
                self.db.chiudi_connessione()
                break
            else:
                print("Scelta non valida.")

    # Funzione inserimento di un voto numerico tra 0 e 10
    def inserisci_voto(self, materia):

        self.visualizza_studenti()

        id = input("Inserisci ID studente: ")

        while True:
            try:
                voto = float(input(f"Voto {materia}: "))
                if 0 <= voto <= 10:
                    return voto
                else:
                    print("Il voto deve essere compreso tra 0 e 10.")

            except:
                print("Inserisci un numero valido.")

    # Inserimento di uno studente 
    def inserisci(self):
        while True:
            nome = input("Nome studente: ").strip()
            if nome.isalpha():
                break
            print("Il nome deve contenere solo lettere.")

        italiano = self.inserisci_voto("italiano")
        matematica = self.inserisci_voto("matematica")
        self.db.inserisci_studente(nome, italiano, matematica)
        print("Studente inserito con successo.")


    # Visualizzazione studenti con media voti
    def visualizza(self):
        studenti = self.db.visualizza_studenti()
        print("\nElenco studenti e medie:")
        for id_studente, nome, italiano, matematica in studenti:
            media = self.calcola_media(italiano, matematica)
            print(f"ID: {id_studente} | {nome} | Italiano: {italiano} | Matematica: {matematica} | Media: {media:.2f}")



    # Modifica studente
    def modifica(self):
        self.visualizza()
        try:
            id_studente = int(input("ID dello studente da modificare: "))
        except:
            print("Inserisci un ID valido.")
            return

        nuovo_nome = input("Nuovo nome: ").strip()
        if not nuovo_nome.isalpha():
            print("Il nome deve contenere solo lettere.")
            return

        nuovo_italiano = self._inserisci_voto("italiano")
        nuovo_matematica = self._inserisci_voto("matematica")
        self.db.modifica_studente(id_studente, nuovo_nome, nuovo_italiano, nuovo_matematica)
        print("Studente modificato con successo.")

    # Eliminazione studente tramite ID
    def elimina(self):
        self.visualizza()
        try:
            id_studente = int(input("ID dello studente da eliminare: "))
            self.db.elimina_studente(id_studente)
            print("Studente eliminato con successo.")
        except ValueError:
            print("Inserisci un ID valido.")
