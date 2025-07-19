def ispalindrome(stringa):
    s = "".join([char for char in stringa if char.isalnum()]) 
    s = s.lower()

    i,j = 0,len(s) - 1
    is_pal = True

    while i<j:
        if s[i] != s[j]:
            is_pal = False
            break
        i += 1
        j -= 1
    print(f"La stringa {stringa} è palindroma") if is_pal else print(f"La stringa {stringa} non è palindroma")

stringa = input("Inserisci una stringa: ")
ispalindrome(stringa)


"""
def è_palindroma(stringa):
    lettere_valide = "abcdefghijklmnopqrstuvwxyz"
    pulita = ""

    for char in stringa.lower():
        if char in lettere_valide:
            pulita += char

    return pulita == pulita[::-1]

# Input utente
frase = input("Inserisci una frase: ")

# Risultato
if è_palindroma(frase):
    print(f"'{frase}' è palindroma.")
else:
    print(f"'{frase}' non è palindroma.")
"""