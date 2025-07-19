"""Create un programma python che permette tramite le api
open meteo(per le previsioni metereologiche) , di visualizzare le previsione
metereologiche.
L’utente potrà scegliere la cità e se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni."""

import requests
#import json

def set_citta(citta):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json"
    response = requests.get(url)
    data = response.json()
    
    if "results" in data and len(data["results"]) > 0:
        result = data["results"][0]
        return result["latitude"], result["longitude"], result["name"], result.get("country", "")
    else:
        return None, None, None, None

def set_giorni():
    while True:
        try:
            giorni = int(input("Quanti giorni di previsioni vuoi vedere? (1, 3 o 7): "))
            if giorni in [1, 3, 7]:
                return giorni
            else:
                print(" Inserisci solo 1, 3 o 7.")
        except ValueError:
            print(" Inserisci un numero valido (1, 3 o 7).")

def set_visualizzazione():
    print("\nVuoi visualizzare i seguenti dati? (s/n)")
    temperatura = input(" Temperatura: ").strip().lower() == 's'
    vento = input(" Vento: ").strip().lower() == 's'
    precipitazioni = input(" Precipitazioni: ").strip().lower() == 's'
    return precipitazioni, vento, temperatura

def mostra_previsioni(lat, lon, giorni, mostra_temp, mostra_vento, mostra_precip):
    # Prepariamo i parametri
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [],
        "timezone": "auto"
    }

    if mostra_temp:
        params["daily"].append("temperature_2m_max")
        params["daily"].append("temperature_2m_min")
    if mostra_vento:
        params["daily"].append("windspeed_10m_max")
    if mostra_precip:
        params["daily"].append("precipitation_sum")

    # Converti lista in stringa separata da virgole
    params["daily"] = ",".join(params["daily"])

    url = "https://api.open-meteo.com/v1/forecast"
    response = requests.get(url, params=params)
    data = response.json()

    print("\nPrevisioni meteo:\n")
    giorni_disponibili = len(data["daily"]["time"])
    giorni = min(giorni, giorni_disponibili)

    for i in range(giorni):
        print(f"Giorno {i+1} - {data['daily']['time'][i]}")

        if mostra_temp:
            print(f"Temperatura max: {data['daily']['temperature_2m_max'][i]}°C")
            print(f"Temperatura min: {data['daily']['temperature_2m_min'][i]}°C")
        if mostra_vento:
            print(f" Vento max: {data['daily']['windspeed_10m_max'][i]} km/h")
        if mostra_precip:
            print(f"Precipitazioni: {data['daily']['precipitation_sum'][i]} mm")

        print("-" * 30)

def main():
    print("=== PREVISIONI METEO CON OPEN-METEO ===\n")
    citta = input("Inserisci il nome della città: ")
    lat, lon, nome_uff, paese = set_citta(citta)

    if lat is None:
        print("Città non trovata.")
        return

    print(f"Hai scelto: {nome_uff}, {paese} (lat: {lat}, lon: {lon})")

    giorni = set_giorni()
    precipitazioni, vento, temperatura = set_visualizzazione()

    mostra_previsioni(lat, lon, giorni, temperatura, vento, precipitazioni)

if __name__ == "__main__":
    main()
