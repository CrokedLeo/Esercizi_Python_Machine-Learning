def caesar_en(stringa:str, k:int, switch:bool):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = stringa.lower()

    if switch:
        for i in range(len(s)):
            index = alphabet.index(s[i])
            s = s.replace(s[i], alphabet[(index + k)%26])
        print(s)
    else:
        for i in range(len(s)):
            index = alphabet.index(s[i])
            s = s.replace(s[i], alphabet[(index - k)%26])
        print(s)

parola = input("Dammi una parola: ")
chiave = int(input("Dammi la chiave (un intero tra 1 e 25): "))
op = bool(int(input("Che operazione vuoi fare? (1 per criptare, 0 per decriptare): ")))

caesar_en(parola, chiave, op)
