from soldato import Soldato
import random

class Assassino(Soldato):
    def __init__(self, nome):
        super().__init__(nome, 95, 18, 8, 75)

    def attacca(self, avversario):
        avversario.difenditi(self._attacco)
        print(f"{self._nome} trafigge {avversario._nome} infliggendo {self._attacco} danni!")

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if self._cooldown_abilita == 0 and nemici:
            target = random.choice(nemici)
            target._effetti_attivi["avvelenato"] = 3
            print(f"{self._nome} avvelena {target._nome}!")
            self._cooldown_abilita = 3
