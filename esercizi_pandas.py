import pandas as pd
import numpy as np


#Esercizio 1: Analisi Esplorativa dei Dati
#Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati usando pandas.
#Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su un gruppo di persone: Nome, Età, Città e Salario. 
#Caricare i dati in un DataFrame autogenerandoli casualmente .
#Visualizzare le prime e le ultime cinque righe del DataFrame.
#Visualizzare il tipo di dati di ciascuna colonna.
#Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard).
#Identificare e rimuovere eventuali duplicati.
#Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.
#Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18 anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
#Salvare il DataFrame pulito in un nuovo file CSV.


"""#lista nomi e citta a caso
nomi = ['Anna', 'Luca', 'Marco', 'Giulia', 'Francesca', 'Davide', 'Sara', 'Giorgio', 'Elisa', 'Paolo']
citta = ['Roma', 'Milano', 'Napoli', 'Torino', 'Firenze']

#crea df dataframe 15 righe
data = {
    "nome": [random.choice(nomi) for _ in range(15)],
    "eta" : [random.randint(15,99) for _ in range(15)],
    "citta": [random.choice(citta) for _ in range(15)],
    "salario": [random.randint(1000, 5000) for _ in range(15)]
}

df = pd.DataFrame(data)

# genro duplicato con .loc
df.loc[1]= df.loc[0]
# inserisi valori nan
df.loc[5, "salario"] = np.nan
df.loc[10, "eta"] = np.nan

print(df)


#visualizza primi 5 e ultimi 5
print("prime 5 righe.\n", df.head())
print("ultime 5 righe.\n", df.tail())

#visualizza tipo dati
print("tipo di dati:\n", df.dtypes)

# descrvi media mediana std
print("statisiche:\n")
print("media:\n", df.mean(numeric_only=True))
print("mediana:\n", df.median(numeric_only=True))
print("deviazione\n:", df.std(numeric_only=True))


#rimuovi duplicati
df = df.drop_duplicates()
print("prime 5 righe.\n", df.head())

#sostitusci NAn con fillna con mediana
df["eta"].fillna(df["eta"].median(), inplace=True)
df["salario"].fillna(df["salario"].median(), inplace=True)
print(df)

# categorie givane adulto senior
def categorie(eta):
    if eta <=18:
        return "giovane"
    elif eta <= 65:
        return "adulto"
    else:
        return "senior"
    
#inserisi categorie
df["categoria"] = df["eta"].apply(categorie)

print(df)"""

#Esercizio 1: 
#Crea due liste: una contenente i nomi dei reparti ('Libri', 'Giocattoli') euna con 3 codici prodotto per ciascun reparto (1, 2, 3). 
#Crea un MultiIndex con queste due liste e costruisci un DataFrame che contengauna colonna "Prezzo" con valori casuali.

reparti = ["libri","giocattoli"]
codici = [1, 2, 3]

#crea lista per multiindex
multi_index = pd.MultiIndex.from_product([reparti, codici], names=["reparto", "codice"] )

#genera prezzi
prezzi = np.random.randint(5,100, size=len(multi_index))


df = pd.DataFrame(
    {"prezzo": prezzi}, index=multi_index)

print(df)


#Esercizio 2:
#Hai tre categorie di prodotti ("Elettronica", "Alimentari", "Abbigliamento"),ciascuna con 3 codici identificativi univoci. 
#Costruisci un DataFrame con MultiIndex, e aggiungi colonne "Vendite" e "Sconto". 
#Poi, accedi solo ai dati della categoria "Elettronica" e calcola il valore netto (Vendite - Sconto) per ciascun prodotto.

categorie = ["elettronica","Alimentari","abbigliamento"]
codici = [1, 2, 3]

#crea multiind 
multi_index = pd.MultiIndex.from_product([categorie, codici], names=["categoria", "codice"])

#valori casuali vendite e sconto
vendite = np.random.randint(100, 1000, size=len(multi_index))
sconti = np.random.randint(0, 120, size=len(multi_index))

df= pd.DataFrame({
    "vendite": vendite,
    "sconto": sconti
}, index=multi_index)

print("-----completo-----\n")
print(df)

#solo elettronica
elettronica_df = df.loc["elettronica"].copy()#se no da warning
print(elettronica_df)

#valore vendite - sconto in elettronica
elettronica_df["valore netto"]= elettronica_df["vendite"] - elettronica_df["sconto"]
print("valore netto elettronica:\n")
print(elettronica_df)


#Esercizio 1: 
#Hai tre DataFrame che rappresentano i dati di vendita dei mesi di gennaio, febbraio e marzo. 
#Ogni DataFrame ha due colonne: "Giorno" e "Vendite". Unisci i tre DataFrame in uno solo usando concat.

df_gen = pd.DataFrame({
    "giorno": [1,2,3],
    "vendite": [100,150,200]
})

df_febb = pd.DataFrame({
    "giorno": [1,2,3],
    "vendite": [90,120,210]
})

df_mar = pd.DataFrame({
    "giorno": [1,2,3],
    "vendite": [130,100,170]
})

#unisci dataf.contact
df_tot = pd.concat([df_gen, df_febb, df_mar])
print(df_tot)

#Esercizio 2: 
#Hai un DataFrame con informazioni sugli studenti (ID, Nome) e un altro con i loro voti (ID, Materia, Voto). 
#Unisci i due DataFrame usando merge sulla colonna ID per ottenere un'unica tabella con i voti e i nomi degli studenti.

#crea data
df_studenti = pd.DataFrame({
    "id": [1,2,3],
    "nome": ["anna","marco","bob"]
})
df_voti= pd.DataFrame({
    "id": [1,2,1,3],
    "materia":["matematica","storia","ficica","inglese"],
    "voto": [28,30,21,18]
})
#print(df_studenti,df_voti)

#merge x id
df_completo = pd.merge(df_voti,df_studenti, on="id")
print(df_completo)