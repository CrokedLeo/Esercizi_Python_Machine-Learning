class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False 
        self.menu = {}

    def descrivo_ristorante(self):
        print(f"Ristorante '{self.nome}' di cucina {self.tipo_cucina}.")

    def stato_apertua(self):
        if self.aperto:
            print(f"Il ristorante '{self.nome}' è aperto.")
        else:
            print(f"Il ristorante '{self.nome}' è chiuso.")
    
    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante '{self.nome}' è aperto.")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante '{self.nome}' è chiuso.")

    def aggiungi_piatto(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print(f"Aggiunto '{piatto}' al menu con prezzo {prezzo} euro.")

    def rimuovi_piatto(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"Rimosso '{piatto}' dal menu.")
    
    def stampa_menu(self):
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            print("Menu del ristorante:")
            for piatto, prezzo in self.menu.items():
                print(f"{piatto}: {prezzo} euro")


#main

from ristorante import Ristorante

mio_ristorante = Ristorante("La Pergola", "Cucina Gourmet")

mio_ristorante.descrivo_ristorante()

# Apriamo il ristorante
mio_ristorante.apri_ristorante()
mio_ristorante.stato_apertua()

# Aggiungiamo alcuni piatti
mio_ristorante.aggiungi_piatto("Risotto al tartufo", 25.00)
mio_ristorante.aggiungi_piatto("Spaghetti alla carbonara", 18.50)
mio_ristorante.aggiungi_piatto("Tiramisù", 7.00)

# Stampiamo il menu
mio_ristorante.stampa_menu()

mio_ristorante.rimuovi_piatto("Tiramisù")
mio_ristorante.stampa_menu()

# Chiudiamo il ristorante
mio_ristorante.chiudi_ristorante()
mio_ristorante.stato_apertua()
