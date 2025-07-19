prezzo_base = 500

cliente = {
    "nome": input("Nome cliente: "),
    "età": int(input("Età del conducente: ")),
    "esperienza": int(input("Anni di esperienza alla guida: ")),
    "incidenti": int(input("Numero di incidenti negli ultimi 5 anni: ")),
    "pacchetto": input("Scegli pacchetto assicurativo (Base/Intermedio/Premium): ").lower()
}

if cliente["età"] < 18 or cliente["incidenti"] > 4:
    print("Non sei idoneo per l'assicurazione.")
else:
    prezzo_finale = prezzo_base

    if 18 <= cliente["età"] <= 25:
        prezzo_finale *= 1.20
    elif cliente["età"] > 50:
        prezzo_finale *= 0.90

    if cliente["esperienza"] < 2:
        prezzo_finale *= 1.30

    if cliente["incidenti"] == 1:
        prezzo_finale *= 1.15
    elif cliente["incidenti"] >= 2:
        prezzo_finale *= 1.30

    if cliente["pacchetto"] == "intermedio":
        prezzo_finale *= 1.20
    elif cliente["pacchetto"] == "premium":
        prezzo_finale *= 1.50

    print(f"\nPreventivo per {cliente['nome']}: {prezzo_finale:.2f}€")
