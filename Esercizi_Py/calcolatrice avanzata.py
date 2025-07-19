print("Benvenuto nella calcolatrice avanzata!")
print("Scrivi 'Esci' per chiudere.")

while True:
    espressione = input("Inserisci l'operazione: ")

    if espressione.lower() == "esci":
        print("Chiusura della calcolatrice. A presto!")
        break

    try:
        risultato = eval(espressione)
        print("Risultato:", risultato)
        print("-" * 30)
    except Exception as e:
        print("Errore nell'operazione:", e)
