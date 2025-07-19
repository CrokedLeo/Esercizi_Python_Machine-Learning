from soldato import Soldato

class Arciere(Soldato):
    def __init__(self, nome):
        super().__init__(nome, 80, 15, 5, 70)

    def attacca(self, avversario):
        avversario.difenditi(self._attacco)
        print(f"{self._nome} colpisce {avversario._nome} con una freccia infliggendo {self._attacco} danni!")

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if self._cooldown_abilita == 0 and nemici:
            print(f"{self._nome} scocca una raffica di frecce!")
            for nemico in nemici:
                nemico.difenditi(int(self._attacco / 2))
            self._cooldown_abilita = 3
