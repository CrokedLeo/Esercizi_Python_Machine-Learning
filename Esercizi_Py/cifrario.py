def cifrario(testo, chiave, modalità):
    risultato = ""

    for char in testo:
        if char.isalpha():
            shift = ord(chiave.lower()) - ord('0')
            if modalità == 'decifrare':
                shift = -shift
            
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            nuovo_char = chr((ord(char) - base + shift) % 26 + base)
            risultato += nuovo_char
        else:
            risultato += char

    return risultato

modalità = input("Vuoi cifrare o decifrare? (cifrare/decifrare): ").strip().lower()
messaggio = input("Inserisci il testo: ")
chiave = input("Inserisci la chiave (una lettera): ").strip()

