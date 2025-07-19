'''
Create un programma python che permette tramite le api
open meteo(per le previsioni metereologiche) , di visualizzare le previsione
metereologiche.
L utente potrà scegliere la cità e se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni.
'''
#temporal resolution: 3 hours
import requests 

# funzione per estrapolare latitudine e longitudine della città selezionata
def lat_long_citta(citta):
    url_citta = f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json"
    try: 
        response = requests.get(url_citta)
        dictResp = response.json()#trasformo in dizionare
        latitudine = dictResp["results"][0]["latitude"]
        longitudine = dictResp["results"][0]["longitude"]
        return latitudine, longitudine
    except: 
        print("Problemi di connessione all'API o città inserita non valida")
        return None, None
        

# funzione per previsioni meteo temperatura
def previsioni_temp(latitudine, longitudine, scelta_giorni):
    url_previsioni = f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&hourly=temperature_2m&forecast_days={scelta_giorni}&temporal_resolution=hourly_3"
    try:
        response = requests.get(url_previsioni)
        dictResp = response.json()
        for i in range(len(dictResp["hourly"]["time"])):
            print(f"giorno: {dictResp["hourly"]["time"][i]}, temperatura: {dictResp["hourly"]["temperature_2m"][i]} °C")
    except: print("Impossibile visualizzare previsioni temperature!")
        
# funzione per previsioni meteo temperatura + velocità del vento
def previsioni_temp_vento(latitudine, longitudine, scelta_giorni):
    url_previsioni = f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&hourly=temperature_2m,wind_speed_10m&forecast_days={scelta_giorni}&temporal_resolution=hourly_3"
    try:
        response = requests.get(url_previsioni)
        dictResp = response.json()
        for i in range(len(dictResp["hourly"]["time"])):
            print(f"giorno: {dictResp["hourly"]["time"][i]}, temperatura: {dictResp["hourly"]["temperature_2m"][i]} °C, velocità del vento: {dictResp["hourly"]["wind_speed_10m"][i]} km/h")
    except: print("Impossibile visualizzare previsioni temperature e velocità del vento!")

# funzione per previsioni meteo temperatura + probabilità precipitazioni
def previsioni_temp_precip(latitudine, longitudine, scelta_giorni):
    url_previsioni = f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&hourly=temperature_2m,precipitation_probability&forecast_days={scelta_giorni}&temporal_resolution=hourly_3"
    try:
        response = requests.get(url_previsioni)
        dictResp = response.json()
        for i in range(len(dictResp["hourly"]["time"])):
            print(f"giorno: {dictResp["hourly"]["time"][i]}, temperatura: {dictResp["hourly"]["temperature_2m"][i]} °C, probabilità precipitazioni: {dictResp["hourly"]["precipitation_probability"][i]} %")
    except: print("Impossibile visualizzare previsioni temperature e probabilità di precipitazioni!")

# funzione per previsioni meteo temperatura + velocità del vento + probabilità precipitazioni
def previsioni_tutto(latitudine, longitudine, scelta_giorni):
    url_previsioni = f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&hourly=temperature_2m,wind_speed_10m,precipitation_probability&forecast_days={scelta_giorni}&temporal_resolution=hourly_3"
    try:
        response = requests.get(url_previsioni)
        dictResp = response.json()
        for i in range(len(dictResp["hourly"]["time"])):
            print(f"giorno: {dictResp["hourly"]["time"][i]}, temperatura: {dictResp["hourly"]["temperature_2m"][i]} °C, velocità del vento: {dictResp["hourly"]["wind_speed_10m"][i]} km/h, probabilità precipitazioni: {dictResp["hourly"]["precipitation_probability"][i]} %")
    except: print("Impossibile visualizzare previsioni temperature, velocità del vento e probabilità di precipitazioni!")


# Menù utente

print("Previsioni metereologiche!")
while True:
    citta = input("Di quale città vuoi le previsioni meteo? ")
    if not citta.isalpha():
        print("Non hai inserito una città! Inserisci solo valori validi")
    else: 
        latitudine, longitudine = lat_long_citta(citta)
        if latitudine == None: #and longitudine == None:
            continue
        num_giorni = int(input("Di quanti giorni vuoi la previsione meteo? (1,3,7): "))
        if num_giorni not in (1,3,7):
            print("Valore non valido, puoi scegliere solo 1 giorno, 3 o 7 giorni!")
            continue
        else:
            scelta = int(input("1) previsioni meteo di temperatura\n2) previsioni meteo di temperatura + velocità del vento\n3) previsioni meteo di temperatura + probabilità precipitazioni\n4) previsioni meteo complete\n5) exit\n "))
            if scelta == 1:
                previsioni_temp(latitudine,longitudine,num_giorni)
                break
            elif scelta == 2:
                previsioni_temp_vento(latitudine,longitudine,num_giorni)
                break
            elif scelta == 3:
                previsioni_temp_precip(latitudine,longitudine,num_giorni)
                break
            elif scelta == 4:
                previsioni_tutto(latitudine,longitudine,num_giorni)
                break
            elif scelta == 5:
                print("Arrivederci!")
                break
            else: 
                print("Numero inserito non valido!")
                continue

