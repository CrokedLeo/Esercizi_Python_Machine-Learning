eta = int(input("Quanti anni hai? "))
patente = input("Hai la patente? (sì/no): ")
bevuto = input("Hai bevuto alcolici? (sì/no): ")



if eta < 18:
    print("Non puoi guidare: sei minorenne.")
elif patente == "no":
    print("Non puoi guidare: non hai la patente.")
elif bevuto == "si":
    print("Non puoi guidare: hai bevuto alcolici.")
else:
    print("Puoi guidare!")

