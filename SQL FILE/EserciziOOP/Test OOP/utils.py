from cavaliere import Cavaliere
from arciere import Arciere
from guaritore import Guaritore
from mago import Mago
from assassino import Assassino
import random

def crea_soldato(tipo, nome):
    classi = {
        "cavaliere": Cavaliere,
        "arciere": Arciere,
        "guaritore": Guaritore,
        "mago": Mago,
        "assassino": Assassino
    }
    return classi[tipo.lower()](nome)

def acquista_esercito(budget):
    esercito = []
    while budget > 0:
        print(f"\nBudget rimanente: {budget}")
        scelta = input("Scegli un soldato (Cavaliere, Arciere, Guaritore, Mago, Assassino) o 'fine': ").lower()
        if scelta == "fine":
            break
        nome = input("Dai un nome al tuo soldato: ")
        try:
            soldato = crea_soldato(scelta, nome)
            if soldato._costo <= budget:
                esercito.append(soldato)
                budget -= soldato._costo
            else:
                print("Budget insufficiente per questo soldato.")
        except KeyError:
            print("Tipo di soldato non valido.")
    return esercito, budget

def skynet_acquisto(budget):
    esercito = []
    tipi = [Cavaliere, Arciere, Guaritore, Mago, Assassino]
    while budget >= 80:
        tipo = random.choice(tipi)
        soldato = tipo(tipo.__name__ + str(len(esercito)))
        if soldato._costo <= budget:
            esercito.append(soldato)
            budget -= soldato._costo
    return esercito, budget
