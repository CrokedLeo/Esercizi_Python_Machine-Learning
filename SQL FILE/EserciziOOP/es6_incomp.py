class MenboroSquadra:
    def __init__ (self, nome, eta):
        self.nome = nome
        self.eta= eta

    def descrivi(self):
        print(f"{self.nome}, età:{self.eta}")

class Giocatore(MenboroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)

        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def descrivi(self):
        print(f"{self.nome}, {self.eta} anni - giocatore ({self.ruolo}) - maglia n°{self.numero_maglia}")
    
    def gioca_partita(self):
        print(f"{self.nome} sta giocando come {self.ruolo} con la maglia numero {self.numero_maglia}.")


class Allenatore(MenboroSquadra):
    def __init__(self, nome, eta, anni_exp):
        super().__init__(nome, eta)
        self.anni_exp = anni_exp

    def descrivi(self):
        print(f"{self.nome},{self.eta}")
