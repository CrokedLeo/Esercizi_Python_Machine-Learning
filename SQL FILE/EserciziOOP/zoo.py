from abc import ABC, abstractmethod

class Animale(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def verso(self):
        pass

    @abstractmethod
    def mangia(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome}"
    
class Leone(Animale):
    def verso(self):
        return "Ruggisce!"

    def mangia(self):
        return "Mangia carne."

class Elefante(Animale):
    def verso(self):
        return "Barrita!"

    def mangia(self):
        return "Mangia erba e frutta."

class Scimmia(Animale):
    def verso(self):
        return "Urla e strilla!"

    def mangia(self):
        return "Mangia banane e insetti."


class Zoo:
    def __init__(self):
        self.animali = []

    def aggiungi_animale(self, animale):
        self.animali.append(animale)
        print(f"Aggiunto {animale}")

    def rimuovi_animale(self, nome):
        for a in self.animali:
            if a.nome == nome:
                self.animali.remove(a)
                print(f"Rimosso {a}")
                return
        print("Animale non trovato.")

    def mostra_animali(self):
        print("\n--- Animali nello zoo ---")
        for a in self.animali:
            print(f"{a} - {a.verso()} - {a.mangia()}")


def interfaccia_zoo():
    zoo = Zoo()

    while True:
        print("\n--- MENU ZOO ---")
        print("1. Aggiungi animale")
        print("2. Rimuovi animale")
        print("3. Mostra animali")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            nome = input("Nome animale: ")
            print("Tipo: 1) Leone  2) Elefante  3) Scimmia")
            tipo = input("Scelta tipo: ")

            if tipo == "1":
                zoo.aggiungi_animale(Leone(nome))
            elif tipo == "2":
                zoo.aggiungi_animale(Elefante(nome))
            elif tipo == "3":
                zoo.aggiungi_animale(Scimmia(nome))
            else:
                print("Tipo non valido.")

        elif scelta == "2":
            nome = input("Nome dell'animale da rimuovere: ")
            zoo.rimuovi_animale(nome)

        elif scelta == "3":
            zoo.mostra_animali()

        elif scelta == "0":
            print("Chiusura del programma.")
            break
        else:
            print("Scelta non valida.")

# Avvia l'interfaccia se eseguito direttamente
if __name__ == "__main__":
    interfaccia_zoo()
