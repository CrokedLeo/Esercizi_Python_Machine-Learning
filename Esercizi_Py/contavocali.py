parola = input("inserisci parola: ")

vocali = "aeiouAEIOU"

                  #da oggetto numerato
for n, lettera in enumerate(parola):
    
    if lettera in vocali:
        print(f"vocale '{lettera}' in posizione {n}")



#correzione in callasse 
"""count= 0
for lettera in parola:
    if lettera in vocali:
        count += 1

if lettera in vocali:print("non
        print(f"vocale '{lettera}' in posizione {count}")"""
