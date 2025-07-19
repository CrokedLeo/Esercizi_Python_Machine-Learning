from soldato import Soldato
from golem import Golem
import random

class Mago(Soldato):
    def __init__(self, nome):
        super().__init__(nome, 110, 25, 5, 60)

    def attacca(self, avversario):
        if random.random() < 0.25:
            print(f"{self._nome} prova a lanciare una magia, ma fallisce!")
        else:
            danno = random.randint(10, self._attacco)
            avversario.difenditi(danno)
            print(f"{self._nome} lancia una magia su {avversario._nome} infliggendo {danno} danni!")

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if self._cooldown_abilita == 0 and alleati is not None:
            golem = Golem(self._nome + "_Golem")
            alleati.append(golem)
            self._cooldown_abilita = 4
            print(f"{self._nome} evoca un Golem per combattere al suo fianco!")
