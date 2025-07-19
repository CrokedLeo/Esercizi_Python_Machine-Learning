"""
import json

datiJ ='{"name":"tommaso","surname":"muraca"}'
#print(datiJ["name"])
dictDati = {"nome":"tommaso","cognome":"muraca","via":"via roma"}
def convertiJson(datiJ):
    dictDatiJ= json.loads(datiJ)
    print(dictDatiJ["name"])

def convertiDict(dictDati):

    jsonDati = json.dumps(dictDati)
    print(type(jsonDati),jsonDati)

#convertiJson(datiJ)
convertiDict(dictDati)
"""
#import json
import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&forecast_days=3&forecast_hours=24&temporal_resolution=hourly_6"
response = requests.get(url)
#response = requests.request("GET", "https://www.google.it)
#dictResponse = json.loads(response.text)
dictResponse = response.json()
#print(dictResponse["hourly"])
for i in range(len(dictResponse["hourly"]["time"])):
    print(f"giorno:{dictResponse["hourly"]["time"][i]}, temperatura:{dictResponse["hourly"]["temperature_2m"][i]} centigradi")
