num = int(input("Inserisci un numero: "))
i = 1


print(f"Tabellina del {num}:")
while i <= 10:
    risultato = num * i
    print(f"{num} x {i} = {risultato}")
    i += 1