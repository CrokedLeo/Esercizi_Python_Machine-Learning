from soldato import Soldato
import random

class Cavaliere(Soldato):
    def __init__(self, nome):
        super().__init__(nome, 100, 20, 15, 100)
        self._assorbi_danno = False

    def attacca(self, avversario):
        critico = random.random() < 0.2
        danno = self._attacco * 2 if critico else self._attacco
        avversario.difenditi(danno)
        print(f"{self._nome} attacca {avversario._nome} infliggendo {danno} danni!")

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if self._cooldown_abilita == 0:
            self._assorbi_danno = True
            self._cooldown_abilita = 3
            print(f"{self._nome} alza lo scudo e sarà protetto dal prossimo attacco!")
