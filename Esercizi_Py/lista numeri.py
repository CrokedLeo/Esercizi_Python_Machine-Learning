
numeri_input = input("inserisci lista di numeri separati da virgola: ")

numeri = []
for num in numeri_input.split(','):
    numeri.append(int(num.strip()))

print("\nsequenza:")

for i, posizione in enumerate(numeri):
    stella = '*' * posizione
    print(f"{posizione}:{stella}")

