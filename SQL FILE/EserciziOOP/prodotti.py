class Prodotto:
    def __init__(self, nome, costo_prod, prezzo_ven, quantita=1):
        self.nome = nome
        self.costo_prod = costo_prod
        self.prezzo_ven = prezzo_ven
        self.quantita = quantita

    def calcola_profitto(self):
        return (self.prezzo_ven - self.costo_prod) * self.quantita

    def descrizione(self):
        return f"{self.nome} | Costo: euro{self.costo_prod} | Prezzo: euro{self.prezzo_ven} | Quantità: {self.quantita}"

class Elettronica(Prodotto):
    def __init__(self, nome, costo_prod, prezzo_ven, garanzia, quantita=1):
        super().__init__(nome, costo_prod, prezzo_ven, quantita)
        self.garanzia = garanzia

    def descrizione(self):
        return f"[ELETTRONICA] {super().descrizione()} | Garanzia: {self.garanzia} anni"

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_prod, prezzo_ven, taglia, quantita=1):
        super().__init__(nome, costo_prod, prezzo_ven, quantita)
        self.taglia = taglia

    def descrizione(self):
        return f"[ABBIGLIAMENTO] {super().descrizione()} | Taglia: {self.taglia}"
