# main.py

from utils import acquista_esercito, skynet_acquisto
from combattimento import scontro_round

def main():
    budget_gio = budget_sky = 1000
    esercito_gio, budget_gio = acquista_esercito(budget_gio)
    esercito_sky, budget_sky = skynet_acquisto(budget_sky)

    round_num = 0
    while esercito_gio and esercito_sky:
        round_num += 1
        scontro_round(esercito_gio, esercito_sky)

        if not esercito_gio or not esercito_sky:
            break

        print("\nFine dello scontro! Ogni fazione riceve +300 dobloni")
        budget_gio += 300
        budget_sky += 300

        nuovo_esercito_gio, budget_gio = acquista_esercito(budget_gio)
        esercito_gio.extend(nuovo_esercito_gio)

        nuovo_esercito_sky, budget_sky = skynet_acquisto(budget_sky)
        esercito_sky.extend(nuovo_esercito_sky)

    print("\n-Fine della Guerra-")
    vincitore = "Giocatore" if esercito_gio else "SkyNet"

    print(f"Vittoria di: {vincitore}")
    print(f"Schermaglie avvenute: {round_num}")
    print(f"Soldati sopravvissuti nel regno: {len(esercito_gio)}")
    print(f"Soldati sopravvissuti di Skynet: {len(esercito_sky)}")

if __name__ == "__main__":
    main()
