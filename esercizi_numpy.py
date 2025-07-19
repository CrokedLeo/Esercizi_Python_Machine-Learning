
import numpy as np
"""
# crea un array intero da 10 a 49
array = np.arange(10, 50)
print("Array:", array)


# verifica il tipo di dato (dtype) e stampa il risultato
print("Tipo di dato iniziale:", array.dtype)

# cambia il tipo di dato in float64 e verifica di nuovo
array_float = array.astype(np.float64)
print("Array float64:", array_float)
print("Nuovo tipo di dato:", array_float.dtype)

# stampa la forma dell'array
print("Forma dell'array:", array_float.shape)
"""
#Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.#
#Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
#Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
#Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
#Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
#Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
#Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
#Obiettivo:Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.
"""
array = np.random.randint(10, 51, size=20)
print("\n arr originale:\n", array )

#estrai primi 10
primi10 = array[:10]
print("\n primi 10:\n", primi10)

#ultimi 5
ultimi5 = array[-5:]
print("\n ultimi 5:\n", ultimi5)

#dall 5 al 15 escluso
da5a15 = array[5:15]
print("\n elementi dal5 al 15:\n", da5a15)

#ogni terzo elemento
ogniterzo = array [2::3]
print("\n ogni terzo: \n", ogniterzo)

#mdifica da 5 a 10 esl mdifica a 99
array[5:10] = 99
print("\n modifica con slicing:\n", array)
"""

#Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
#Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
#Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
#Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
#Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
#Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.
#Obiettivo:Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi.

"""#crea 6x6 da 1 a 100
matrice =  np.random.randint(1,101, size=(6,6))
print("matrice 6x6:\n" , matrice)

#sorttomatrice centrale 4x4
sottmat = matrice[1:5, 1:5]
print("sottomatrice 4x4:\n", sottmat)

#inverti sottmat
sotmatinv = sottmat[::-1]
print("sottomatrice invertita: \n", sotmatinv)

#diagonale matinv
diagonale = np.diag(sotmatinv)
#diagonale = []
#for i in range(len(sotmatinv)):
#    diagonale.append(sotmatinv[i][i])

print("diaconale : \n", diagonale)

#sostituisci multipli 3 con -1
sotmatmod = np.where(  #funz elementi dip dalla condizione
   sotmatinv % 3 == 0,
    -1, sotmatinv)


print("sotmat sostituita: \n" , sotmatmod)"""

#Esercizio 1: Somma e Media di Elementi
#Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
#Calcolare e stampare la somma di tutti gli elementi dell'array.
#Calcolare e stampare la media di tutti gli elementi dell'array.

"""arr1 = np.random.randint(1,101, size=15)
print("originale:\n",arr1)
#somma
somma = np.sum(arr1)
print("somma:\n", somma)
#media
media = np.mean(arr1)
print("media:\n", media)"""



#Esercizio 2: Manipolazione di Array Multidimensionali
#Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
#Estrarre e stampare la seconda colonna della matrice.
#Estrarre e stampare la terza riga della matrice.
#Calcolare e stampare la somma degli elementi della diagonale principale della matrice.

"""matrice = np.arange(1,26).reshape(5, 5)
print("martice5x5:\n", matrice)

#seconda colonna ind 1
secondcol =matrice[:,1]
print("seconda colonna:\n", secondcol)

#terza riga ind2
terzriga = matrice[2,:]
print("terza riga:\n", terzriga)

#somma diagonale
#print("somma diag:\n", matrice.diagonal().sum())
sommdiag = np.trace(matrice) #Return the sum along diagonals of the array.
print("somma diagonale:\n", sommdiag)"""


#Esercizio 3: Operazioni con Fancy Indexing
#Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
#Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
#Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).
#Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.

"""arr2 = np.random.randint(10, 51,size=(4,4))
print("array 4x4:\n", arr2)

#selez elementi con fancyinex
righe = [0,1,2,3]
colonne= [1,3,2,0]
selez = arr2[righe, colonne]
print("selezione spec:", selez)

#selez righe dispari ind 1e3
rigdisp = arr2[1::2]
print ("righe dispari:\n", rigdisp)

#modficia con agg di 10
arr2 [righe, colonne]+= 10
print("aggiunta di 10 a elementi:\n", arr2)"""


#concatenare piu array in np
#dividere array array_split
#ordinare valori nell'array con SORT

"""a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Concatenate\n")
result = np.concatenate((a, b), axis=0)
print(result)

resultColonne = np.concatenate((a,b), axis=1)
print("\n", resultColonne)

print("\n Split \n")

result_split_perfetto = np.array_split(result, 4)

print("Result split perfetto: \n", result_split_perfetto)

result_split_nonperfetto = np.array_split(result, 3)

print("Result split imperfetto: \n", result_split_nonperfetto)

c = np.array([1,2,3,4,5,6,7])

imp = np.array_split(c, 3)

print("Imp: \n", imp)

print("\nSORT\n")

d = np.random.randint(0, 11, 10)

print(d)
print("\n")
print(np.sort(d)[::-1])

arr2d = np.array([[3,2,1],[6,5,4]])
oredered2d = np.sort(arr2d, axis = 1)
print("\n 2d sort: \n", oredered2d)"""


#1)Create due array (voti_classe1 e voti_classe2) con 10 voti casuali ciascuno, valori tra 18 e 30.
#2)Concatenate i due array per creare un unico array chiamato tutti_voti.
#3)Dividete tutti_voti in 5 sottogruppi (es. gruppi studio) usando np.array_split.
#4)Ordinate ciascun sottogruppo in ordine crescente.
#5)Stampate in modo chiaro:
#- Array completo dei voti concatenati
#- Lista ordinata dei voti per ciascun gruppo
#- Media voto totale e media voto per ciascun gruppo (opzionale, suggerimento extra).

"""#arry x10voti
classe1 = np.random.randint(18,31, size=10)
classe2 = np.random.randint(18,31, size=10)

#concatenate
tutti = np.concatenate((classe1, classe2))

#dividi in 5 array_split
gruppi = np.array_split(tutti ,5)

#ordina con sort
gruppiord = [np.sort(gruppo)for gruppo in gruppi]

#stampe
print("tutti i voti")
print(classe1)
print(classe2)

print(" voti concatenati")
print(tutti)

print("voti ordinatiper gruppo")
for i, gruppo in enumerate(gruppi, start= 1):
    print(f"gruppo {i}: {gruppo}")

#medie
mediatot = np.mean(tutti)
print(f"media totale: {mediatot}")

for i,gruppo in enumerate(gruppiord, start=1):
    mediagrup = np.mean(gruppo)
    print(f"media gruppo {i}: {mediagrup}")"""