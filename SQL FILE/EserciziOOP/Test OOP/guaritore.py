from soldato import Soldato
import random

class Guaritore(Soldato):
    def __init__(self, nome):
        super().__init__(nome, 90, 5, 5, 80)
        self._resurrezione_usata = False

    def attacca(self, avversario):
        avversario.difenditi(self._attacco)
        print(f"{self._nome} colpisce {avversario._nome} infliggendo {self._attacco} danni!")

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if alleati:
            vivi = [s for s in alleati if s != self and s.e_vivo()]
            if vivi:
                target = random.choice(vivi)
                cura = 20
                target._salute = min(target._salute + cura, target._salute_massima)
                print(f"{self._nome} cura {target._nome} di {cura} HP!")

        if not self._resurrezione_usata and alleati:
            morti = [s for s in alleati if not s.e_vivo()]
            if morti:
                resuscitato = random.choice(morti)
                resuscitato._salute = int(resuscitato._salute_massima / 2)
                self._resurrezione_usata = True
                print(f"{self._nome} resuscita {resuscitato._nome} con {resuscitato._salute} HP!")
