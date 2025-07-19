from abc import ABC


class Veicolo(ABC):
    def __init__(self, marca, modello, anno):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False

    def accendi(self):
        if not self._accensione:
            self._accensione = True
            print(f"{self._marca} {self._modello} accesa")
        else:
            print(f"{self._marca} {self._modello} è già accesa")

    def spegni(self):
        if self._accensione:
            self._accensione = False
            print(f"{self._marca} {self._modello} spenta")
        else:
            print(f"{self._marca} {self._modello} è già spenta")

    def __str__(self):
        stato = "accesa" if self._accensione else "spenta"
        return f"{self._anno} {self._marca} {self._modello} '{stato}'"


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self._numero_porte = numero_porte

    def suona(self):
        print(f"{self._marca} {self._modello}: BEEP!")


class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita_carico):
        super().__init__(marca, modello, anno)
        self._capacita_carico = capacita_carico
        self._carico_attuale = 0

    def carica(self, peso):
        if self._carico_attuale + peso <= self._capacita_carico:
            self._carico_attuale += peso
            print(f"Carico di {peso}kg effettuato. Totale: {self._carico_attuale}kg")
        else:
            print("Carico troppo pesante!")

    def scarica(self):
        print(f"Scarico di {self._carico_attuale}kg completato.")
        self._carico_attuale = 0


class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self._tipo = tipo.lower()

    def impenna(self):
        if self._tipo == "sportivo":
            print(f"{self._marca} {self._modello} fa un'impennata!")
        else:
            print(f"{self._marca} {self._modello} non è adatta a impennare.")


class GestioneVeicoli:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self._veicoli.append(veicolo)
        print(f"Aggiunto: {veicolo}")

    def rimuovi_veicolo(self, marca, modello):
        for v in self._veicoli:
            if v._marca.lower() == marca.lower() and v._modello.lower() == modello.lower():
                self._veicoli.remove(v)
                print(f"Rimosso: {marca} {modello}")
                return
        print("Veicolo non trovato.")

    def lista_veicoli(self):
        if not self._veicoli:
            print("Non ci sono veicoli.")
        else:
            print("Veicoli disponibili:")
            for v in self._veicoli:
                print("-", v)


# ------ MAIN ------
def main():
    gestore = GestioneVeicoli()

    auto = Auto("Fiat", "Panda", 2000, 5)
    auto2 = Auto("Ferrari", "F40", 1989, 3)

    furgone = Furgone("Fiat", "Ducato", 2018, 2000)
    furgone2 = Furgone("Fiat", "Fiorino", 2014, 1000)

    moto = Moto("Yamaha", "R1", 2020, "sportivo")
    moto2 = Moto("Piaggio", "Vespa", 1984, "classico")

    gestore.aggiungi_veicolo(auto)
    gestore.aggiungi_veicolo(auto2)
    gestore.aggiungi_veicolo(furgone)
    gestore.aggiungi_veicolo(furgone2)
    gestore.aggiungi_veicolo(moto)
    gestore.aggiungi_veicolo(moto2)

    print()
    gestore.lista_veicoli()

    print("\nOperazioni:")
    auto.suona()
    furgone.carica(1000)
    furgone.carica(1200)  # supera capacità
    furgone.scarica()
    moto.impenna()
    moto2.impenna()

    print("\nAccensione veicoli:")
    auto.accendi()
    moto.accendi()
    moto.spegni()

    print("\nRimozione:")
    gestore.rimuovi_veicolo("fiat", "panda")
    gestore.lista_veicoli()


if __name__ == "__main__":
    main()
