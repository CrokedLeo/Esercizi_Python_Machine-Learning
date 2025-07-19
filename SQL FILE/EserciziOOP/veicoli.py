class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.km_percorsi = 0

    def sposta(self, km):
        self.km_percorsi += km
        print(f"{self.marca} {self.modello} ha percorso {km} km (Totale: {self.km_percorsi} km).")


class Auto(Veicolo):
    def __init__(self, marca, modello, cilindrata):
        super().__init__(marca, modello)
        self.cilindrata = cilindrata

    def sposta(self, km):
        print(f"L'auto {self.marca} {self.modello} (cilindrata {self.cilindrata}cc) si sta spostando...")
        super().sposta(km)


class Bicicletta(Veicolo):
    def __init__(self, marca, modello, tipo_pedali):
        super().__init__(marca, modello)
        self.tipo_pedali = tipo_pedali

    def sposta(self, km):
        print(f"La bicicletta {self.marca} {self.modello} con pedali {self.tipo_pedali} si muove pedalando...")
        super().sposta(km)


# Supponi che le classi Veicolo, Auto e Bicicletta siano già definite sopra

def interfaccia_veicoli():
    veicoli = []

    while True:
        print("\n--- MENU VEICOLI ---")
        print("1. Aggiungi Auto")
        print("2. Aggiungi Bicicletta")
        print("3. Sposta veicolo")
        print("4. Mostra tutti i veicoli")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            marca = input("Marca: ")
            modello = input("Modello: ")
            cilindrata = input("Cilindrata: ")
            veicoli.append(Auto(marca, modello, cilindrata))
        elif scelta == "2":
            marca = input("Marca: ")
            modello = input("Modello: ")
            pedali = input("Tipo di pedali: ")
            veicoli.append(Bicicletta(marca, modello, pedali))
        elif scelta == "3":
            for i, v in enumerate(veicoli):
                print(f"{i}: {v.marca} {v.modello} ({v.km_percorsi} km)")
            idx = int(input("Scegli il veicolo da spostare: "))
            km = int(input("Km da percorrere: "))
            if 0 <= idx < len(veicoli):
                veicoli[idx].sposta(km)
        elif scelta == "4":
            for v in veicoli:
                print(f"{v.marca} {v.modello} - {v.km_percorsi} km")
        elif scelta == "0":
            break
        else:
            print("Scelta non valida.")

# interfaccia_veicoli()
