print("Scrivi 'esci' per chiudere, '=' per vedere il risultato.\n")

risultato = None
while True:
    if risultato is None:
        val = input("Inserisci il primo numero: ")
        if val.lower() == "esci":
            print("Uscita dal programma.")
            break
        if val.replace('.', '', 1).isdigit():
            risultato = float(val)
        else:
            print("Numero non valido. Riprova.")
            continue

    operazione = input("Operazione (+, -, *, /) o '=' per risultato: ").strip()
    
    if operazione == "=":
        print("Risultato finale:", risultato)
        risultato = None
        print("-" * 30)
        continue

    if operazione.lower() == "esci":
        print("Uscita dal programma.")
        break

    if operazione not in ["+", "-", "*", "/"]:
        print("Operazione non valida. Usa +, -, *, /, = o esci.")
        continue

    val = input("Inserisci il numero successivo: ")
    if val.lower() == "esci":
        print("Uscita dal programma.")
        break
    if not val.replace('.', '', 1).isdigit():
        print("Numero non valido. Riprova.")
        continue

    numero = float(val)

    if operazione == "+":
        risultato += numero
    elif operazione == "-":
        risultato -= numero
    elif operazione == "*":
        risultato *= numero
    elif operazione == "/":
        if numero == 0:
            print("Errore: divisione per zero. Riprova.")
            continue
        risultato /= numero
