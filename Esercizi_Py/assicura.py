diz = {}
ass = 500
assFinale = 0

while True:
    cliente = input("Inserire nome del Cliente (oppure 'fine' per finire di di ditare): ")
    if cliente == "fine":
        break

    #CALCOLO ETA
    eta = input("Inserire etÃ del guidatore: ")
    if int(eta) < 18:
        print("Non sei idoneo a guidare.")
        continue

    elif int(eta) >=18 and int(eta) <= 25:
        assFinale = ass + ass*0.2

    elif int(eta) > 50:
        assFinale = ass - ass*0.1
    
    #CALCOLO ANNI EXP
    anniExp  = input("Inserire anni di esperienza del guidatore: ")
    if int(anniExp) < 2:
        assFinale = ass + ass*0.3
    
    #CALCOLO NUMERI INCIDENTI
    numInc = input("Inserire numeri di incidenti effetuati: ")
    if int(numInc) == 1:
        assFinale = ass + ass*0.15

    elif int(numInc) >=2 and int(numInc) < 4:
        assFinale = ass + ass*0.3

    elif int(numInc) > 4:
        print("Non sei idoneo per l'assicurazione.")
        continue

    #SCELTA PACCHETTO
    sceltaAss = input("Che pacchetto vuoi usare? (Base, Intermedio e Premium): ")
    if sceltaAss.lower() == "base":
        if assFinale == 0:
            diz.setdefault(cliente, ass)
        else:
            diz.setdefault(cliente, assFinale)
            
    elif sceltaAss.lower() == "intermedio":
        assFinale = ass + ass*0.2
        diz.setdefault(cliente, assFinale)
    
    elif sceltaAss.lower() == "premium":
        assFinale = ass + ass*0.5
        diz.setdefault(cliente, assFinale)

print(diz)
for k, v in diz.items():
    print(f"Nome cliente: {k} Costo assicurazione: {v}")