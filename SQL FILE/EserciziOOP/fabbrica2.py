class Prodotto:
    def __init__(self, nome, costo_prod, prezzo_ven):
        self.nome = nome
        self.costo_prod = costo_prod
        self.prezzo_ven = prezzo_ven

    def calcola_profitto(self):
        return self.prezzo_ven - self.costo_prod
        
    def descrizione(self):
        return f"{self.nome} - Costo: euro {self.costo_prod}, Prezzo: euro {self.prezzo_ven}"


class Elettronica(Prodotto):
    def __init__(self, nome, costo_prod, prezzo_ven, garanzia):
        super().__init__(nome, costo_prod, prezzo_ven)
        self.garanzia = garanzia

    def descrizione(self):
        return f"{super().descrizione()}, Garanzia: {self.garanzia} anni"
    

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_prod, prezzo_ven, taglia):
        super().__init__(nome, costo_prod, prezzo_ven)
        self.taglia = taglia

    def descrizione(self):
        return f"{super().descrizione()}, Taglia: {self.taglia}"


class Fabbrica:
    def __init__(self, budget_iniziale=10000):
        self.inventario = {}  # formato: {nome: {"prodotto": oggetto, "quantità": n}}
        self.budget = budget_iniziale

    def aggiungi_prodotto(self, prodotto, quantita):
        costo_totale = prodotto.costo_prod * quantita
        if self.budget >= costo_totale:
            if prodotto.nome in self.inventario:
                self.inventario[prodotto.nome]["quantità"] += quantita
            else:
                self.inventario[prodotto.nome] = {"prodotto": prodotto, "quantità": quantita}
            self.budget -= costo_totale
            print(f"Aggiunto {quantita} di {prodotto.nome} all'inventario.")
        else:
            print(f"Budget insufficiente per aggiungere {quantita} di {prodotto.nome}. Costo totale: euro {costo_totale}, Budget disponibile: euro {self.budget}")

    def vendi_prodotto(self, prodotto, quantita):
        nome = prodotto.nome
        if nome in self.inventario and self.inventario[nome]["quantità"] >= quantita:
            self.inventario[nome]["quantità"] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            self.budget += profitto
            print(f"Venduti {quantita} di '{nome}'. Profitto totale: euro {profitto}")
        else:
            print(f"Non presente '{nome}' in magazzino o quantità insufficiente.")

    def resi_prodotto(self, prodotto, quantita):
        nome = prodotto.nome
        if nome in self.inventario:
            self.inventario[nome]["quantità"] += quantita
        else:
            self.inventario[nome] = {"prodotto": prodotto, "quantità": quantita}
        print(f"Resi {quantita} di {nome} all'inventario.")

    def mostra_inventario(self):
        print("Inventario:")
        for item in self.inventario.values():
            prodotto = item["prodotto"]
            quantita = item["quantità"]
            print(f"{prodotto.descrizione()} - quantità: {quantita}")

    def mostra_budget(self):
        print(f"Budget attuale: euro {self.budget}")
