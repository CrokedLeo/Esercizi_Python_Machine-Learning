from oggetti import Pozione, Artefatto, Pergamena

class BottegaMagica:
    def __init__(self, oro_start=100):
        self.oro = oro_start
        self.inventario = {
            "Pozioni": [],
            "Artefatti": [],
            "Pergamene": []
        }

    def aggiungi(self, categoria, oggetto_magico):
        if categoria == "Pozioni":
            self.inventario["Pozioni"].append(Pozione(oggetto_magico))
        elif categoria == "Artefatti":
            self.inventario["Artefatti"].append(Artefatto(oggetto_magico))
        elif categoria == "Pergamene":
            self.inventario["Pergamene"].append(Pergamena(oggetto_magico))
        else:
            print("Categoria non valida.")

    def mostra_inventario(self):
        print(f"\nInventario Bottega (Oro: {self.oro})")
        for categoria, lista in self.inventario.items():
            print(f"{categoria}:")
            if not lista:
                print("  Nessun oggetto.")
            for item in lista:
                print(" ", item.oggetto.descrizione())

    def cerca_oggetto(self, nome_oggetto, categoria):
        lista = self.inventario.get(categoria, [])
        for item in lista:
            if item.oggetto.nome.lower() == nome_oggetto.lower():
                return item
        return None

    def vendi(self, nome_oggetto, categoria, quantita):
        item = self.cerca_oggetto(nome_oggetto, categoria)
        if item:
            if item.oggetto.quantita >= quantita:
                item.oggetto.quantita -= quantita
                guadagno = quantita * item.oggetto.prezzo
                self.oro += guadagno
                print(f"Venduto {quantita} {nome_oggetto} per {guadagno} oro.")
                
                if item.oggetto.quantita == 0:
                    self.inventario[categoria].remove(item)
                    print(f"{nome_oggetto} rimosso dall'inventario.")
            
            else:
                print("Quantità non disponibile.")
        else:
            print("Oggetto non trovato.")

    def reso(self, nome_oggetto, categoria, quantita):
        item = self.cerca_oggetto(nome_oggetto, categoria)
        
        if item:
            item.oggetto.quantita += quantita
            self.oro -= quantita * item.oggetto.prezzo
            print(f"Reso di {quantita} {nome_oggetto}. Oro attuale: {self.oro}")
        else:
            print("Oggetto non trovato.")
