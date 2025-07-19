# Giocatore 1 inserisce numero segreto
numeriere = int(input("Dai dimmi un numero da 1 a 100: "))

# pulisce lo schermo 
print("\n" * 50)

print("Giocatela! Hai 5 tentativi!")

# Inizializza tentativi
tentativi = 0
max_tentativi = 5

# ciclo principale
while tentativi < max_tentativi:
    risposta = input(f"Tentativo {tentativi + 1}: Indovina il numero: ")

    # giocatore si arrende
    if risposta.lower() == "mi arrendo":
        print("che munnezza! era il:", numeriere)
        break

    try:
        # converte in numero
        player = int(risposta)

        # controllo numero
        if player == numeriere:
            print("Complimenti! Hai indovinato il numero! Cacciane 6!")
            break
        elif player < numeriere:
            print("Troppo basso")
        else:
            print("Troppo alto")

        # tentativi usati +1
        tentativi += 1

    except ValueError:
        #  se input non è un numero valido
        print("Inserisci un numero valido o scrivi 'mi arrendo' se hai paura.")

# se hai perso 
if tentativi == max_tentativi and risposta.lower() != "mi arrendo":
    print("peccato cu hai provato! Il numero era:", numeriere)


print("Grazie per aver giocato!")
