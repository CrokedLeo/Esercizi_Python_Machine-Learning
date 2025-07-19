class OggettoMagico:
    def __init__(self, nome, potere, prezzo, quantita):
        self.nome = nome
        self.potere = potere
        self.prezzo = prezzo
        self.quantita = quantita

    def descrizione(self):
        return f"{self.nome}, Potere: {self.potere}, Prezzo: {self.prezzo}, Quantità: {self.quantita}"
    
class Pozione:
    def __init__(self, oggetto):
        self.oggetto = oggetto

class Artefatto:
    def __init__(self, oggetto):
        self.oggetto = oggetto

class Pergamena:
    def __init__(self, oggetto):
        self.oggetto = oggetto
