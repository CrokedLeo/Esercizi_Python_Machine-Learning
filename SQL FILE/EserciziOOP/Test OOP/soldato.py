from abc import ABC, abstractmethod

class Soldato(ABC):
    def __init__(self, nome, costo, attacco, difesa, salute):
        self._nome = nome
        self._costo = costo
        self._attacco = attacco
        self._difesa = difesa
        self._salute = salute
        self._salute_massima = salute
        self._cooldown_abilita = 0
        self._effetti_attivi = {}

    def difenditi(self, danno):
        if hasattr(self, "_assorbi_danno") and self._assorbi_danno:
            danno = int(danno / 2)
            self._assorbi_danno = False
        danno_effettivo = max(0, danno - self._difesa)
        self._salute -= danno_effettivo

    def e_vivo(self):
        return self._salute > 0

    def stato(self):
        indice_salute = self._salute / self._salute_massima
        barra = "█" * int(20 * indice_salute) + "-" * (20 - int(20 * indice_salute))
        print(f"{self._nome} ({self.__class__.__name__}) | {self._salute}/{self._salute_massima} HP [{barra}]")

    def aggiorna_effetti(self):
        for effetto, durata in list(self._effetti_attivi.items()):
            if effetto == "avvelenato":
                danno = 3
                self._salute -= danno
                print(f"{self._nome} subisce {danno} danni da veleno!")
            self._effetti_attivi[effetto] -= 1
            if self._effetti_attivi[effetto] <= 0:
                del self._effetti_attivi[effetto]

    def turno_inizio(self):
        if self._cooldown_abilita > 0:
            self._cooldown_abilita -= 1
        self.aggiorna_effetti()

    @abstractmethod
    def attacca(self, avversario):
        pass

    @abstractmethod
    def usa_abilita_speciale(self, alleati=None, nemici=None):
        pass
