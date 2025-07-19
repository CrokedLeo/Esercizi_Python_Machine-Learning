

class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"{self.nome} si muove con {self.numero_soldati} unità")

    def attacca(self):
        print(f"{self.nome} attacca!!!")

    def ritira(self):
        print(f"{self.nome} si salvi chi puo!")






class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"{self.nome} scava trincee")


class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"{self.nome} lucida i cannoni")


class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"{self.nome} esplora il territorio")


class SupportoLog(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"{self.nome} rifornisce unità")


class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome} ricognizionano")





class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLog, Ricognizione):

    def __init__(self):
        self.unita_registrate = []

    def registra_unita(self, unita):
        self.unita_registrate.append(unita)
        print(f"Unità {unita.nome} registrata.")

    def mostra_unita(self):
        print("Unità registrate:")
        for unita in self.unita_registrate:
            print(f"{unita.nome} ({unita.__class__.__name__}, Soldati: {unita.numero_soldati})")

    def dettagli_unita(self, nome):
        for unita in self.unita_registrate:
            if unita.nome == nome:
                print(f"\nDettagli unità {unita.nome}:")
                unita.muovi()
                unita.attacca()
                unita.ritira()

                if isinstance(unita, Fanteria):
                    unita.costruisci_trincea()
                if isinstance(unita, Artiglieria):
                    unita.calibra_artiglieria()
                if isinstance(unita, Cavalleria):
                    unita.esplora_terreno()
                if isinstance(unita, SupportoLog):
                    unita.rifornisci_unita()
                if isinstance(unita, Ricognizione):
                    unita.conduci_ricognizione()
                return
        print("Unità non trovata.")




#______main

def main():

    comando = ControlloMilitare()

    u1 = Fanteria("Fanteria A", 100)
    u2 = Artiglieria("Cannoni B", 40)
    u3 = Cavalleria("Cavalleria D", 60)
    u4 = SupportoLog("Supporto E", 30)
    u5 = Ricognizione("Ricognitori Z", 10)

    comando.registra_unita(u1)
    comando.registra_unita(u2)
    comando.registra_unita(u3)
    comando.registra_unita(u4)
    comando.registra_unita(u5)

    comando.mostra_unita()

    print()
    comando.dettagli_unita("Cavalleria D")


if __name__ == "__main__":
    main()
