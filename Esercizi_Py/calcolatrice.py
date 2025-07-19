num1 = float(input("primo numero: "))
op = input("scegli l'operazione: ")
num2 = float(input("secondo numero: "))


if op == "+": risultato = num1 + num2

elif op == "-": risultato = num1 - num2

elif op == "*": risultato = num1 * num2

elif op == "/":
    if num2 != 0: risultato = num1 / num2
    else: risultato = "Errore: divisione per zero"

else:
    risultato = "Operazione non valida"

print("risultato:", risultato)
