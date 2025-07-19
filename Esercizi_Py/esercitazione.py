"""stringa = input("inseriisci una stringa: ")
frequenza = {}
for lettera in stringa:
    if lettera in frequenza:
        frequenza[lettera] += 1
    else:
        frequenza[lettera] = 1

        print("Frequenza lettere: ",frequenza)"""


numero = int(input("Inserisci un numero: "))

quadrtato = numero ** 2

if numero % 2 == 0:
    tipo = "pari"
else:
    tipo = "dispari"

cifre = len(str(abs(numero)))

risultato = {
    "quadrato": quadrtato,
    "pari o dispari": tipo,
    "cifre": cifre
}

print(risultato)