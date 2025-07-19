from prodotti import Elettronica, Abbigliamento

class Fabbrica:
    def __init__(self):
        self.budget = 10000
        self.inventario = {"Elettronica": [], "Abbigliamento": []}

    def _get_lista_tipo(self, tipo):
        tipo_key = tipo.capitalize()
        if tipo_key not in self.inventario:
            print("Tipo non valido.")
            return None
        return self.inventario[tipo_key]

    def aggiungi_prodotto(self):
        tipo = input("Tipo prodotto (Elettronica/Abbigliamento): ").strip().capitalize()
        nome = input("Nome: ")
        costo = float(input("Costo di produzione: "))
        prezzo = float(input("Prezzo di vendita: "))
        quantita = int(input("Quanti ne vuoi aggiungere? "))

        if tipo == "Elettronica":
            garanzia = int(input("Garanzia: "))
            prodotto = Elettronica(nome, costo, prezzo, garanzia, quantita)
        
        elif tipo == "Abbigliamento":
            taglia = input("Taglia: ")
            prodotto = Abbigliamento(nome, costo, prezzo, taglia, quantita)
        else:
            print("Tipo non valido.")
            return

        self.inventario[tipo].append(prodotto)
        self.budget -= costo * quantita
        print(f"Aggiunti {quantita} prodotti '{nome}' in {tipo}. Budget attuale: €{self.budget:.2f}")

    def vendi_prodotto(self):
        tipo = input("Tipo prodotto (Elettronica/Abbigliamento): ").strip().capitalize()
        nome = input("Nome del prodotto: ")
        quantita = int(input("Quanti vuoi vendere? "))

        lista = self._get_lista_tipo(tipo)
        if not lista:
            return

        for prodotto in lista:
            if prodotto.nome == nome:
                if prodotto.quantita >= quantita:
                    prodotto.quantita -= quantita
                    guadagno = (prodotto.prezzo_ven - prodotto.costo_prod) * quantita
                    self.budget += guadagno
                    print(f"Venduti {quantita} '{nome}'. Guadagno: euro{guadagno:.2f} | Budget: euro{self.budget:.2f}")
                    if prodotto.quantita == 0:
                        lista.remove(prodotto)
                    return
                else:
                    print(f"Disponibili solo {prodotto.quantita} unità.")
                    return
        print("Prodotto non trovato.")

    def resi_prodotto(self):
        tipo = input("Tipo prodotto (Elettronica/Abbigliamento): ").strip().capitalize()
        nome = input("Nome del prodotto: ")
        quantita = int(input("Quante unità restituite? "))

        lista = self._get_lista_tipo(tipo)
        if not lista:
            return

        for prodotto in lista:
            if prodotto.nome == nome:
                prodotto.quantita += quantita
                print(f"Resi {quantita} '{nome}'. Nuova quantità: {prodotto.quantita}")
                return

        print("Prodotto non esistente. Aggiungilo.")
        self.aggiungi_prodotto()

    def visualizza_inventario(self):
        print("INVENTARIO")
        for tipo, lista in self.inventario.items():
            print(f"\n{tipo.upper()}:")
            if not lista:
                print("  (vuoto)")
            for p in lista:
                print("-", p.descrizione())
        print(f"\nBudget attuale: euro{self.budget:.2f}")
