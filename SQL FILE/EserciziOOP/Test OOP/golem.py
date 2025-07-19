from soldato import Soldato

class Golem(Soldato):
    def __init__(self, nome):
        super().__init__(nome, 0, 30, 10, 50)
        self._durata = 3

    def attacca(self, avversario):
        avversario.difenditi(self._attacco)
        print(f"{self._nome} colpisce {avversario._nome} con forza infliggendo {self._attacco} danni!")

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        pass

    def aggiorna_turno(self):
        self._durata -= 1
        return self._durata <= 0
