#Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
#Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni sulla matrice. Le operazioni disponibili includono:
#Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
#Estrarre e stampare la sotto-matrice centrale.
#Trasporre la matrice e stamparla.
#Calcolare e stampare la somma di tutti gli elementi della matrice.
#Uscire dal programma.

import numpy as np

#var globale
matrice = None

#1 crea mat 2d
def crea_matrice():
    global matrice
    righe =int(input("N di righe: "))
    colonne = int(input("N colonne: "))
    matrice = np.random.randint(1,101, size=(righe, colonne))
    print("matrice:\n")
    print(matrice)


#1.2 estrai sottomatrice min 4x4
def sotto_matrice():
    global matrice
    if matrice is None:
        print("matrice inesistente")
        return
    righe, colonne = matrice.shape
    if righe <4 or colonne <4: 
        print("matrice troppo piccola")
        return
    start_r =(righe -4) //2 # righa e colonna di partenza
    start_c =(colonne - 4) //2
    print("sotto matrice 4x4:\n", matrice[start_r:start_r+4, start_c:start_c+4])

#1.3 stapa matrice trasposta
def trasp_matrice():
    global matrice 
    if matrice is not None:
        print("matrice trasposta:\n", matrice.T)# T traspone righe in colonne
    else:
        print("matrice inesistente")

#1.4 somma tutti gli elementi
def somma_elementi():
    global matrice 
    if matrice is not None:
        print("somma degli elementi: ", np.sum(matrice))
    else:
        print("matrice inesistente")


#Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
#Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per elemento e stampare il risultato.
#Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti gli elementi della matrice.
#EXTRA:Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la matrice è quadrata).

#2.1 moltiplicazione element wise
def moltip_elementwise():
    global matrice
    if matrice is None:
        print ("matrice inesistente")
        return
    seconda = np.random.randint(1,10, size=matrice.shape)
    print("seconda matrice:\n", seconda)
    print("moltiplica prima per seconda:\n", matrice * seconda)

#2.2 calcolo media
def media_matrice():
    global matrice
    if matrice is not None:
        print("media matcice:\n", np.mean(matrice))
    else:
        print ("matrice inesistente")



#Parte 3: Ulteriore Estensione del Menu Interattivo
#Estendere ulteriormente il programma precedente aggiungendo nuove opzioni al menu per permettere ulteriori operazioni sulla matrice. Le nuove operazioni includono:
#Calcolare la matrice inversa (se la matrice è quadrata e invertibile).
#Applicare una funzione matematica a tutti gli elementi della matrice (ad esempio, sin, cos, exp).
#Filtrare e visualizzare solo gli elementi della matrice che soddisfano una determinata condizione (ad esempio, maggiori di un certo valore).
#RENDERE OGNI PARTE RICHIAMABILE SINGOLARMENTE
#Uscire dal programma.
#Tutti i dati necessari al programma possono essere randomizzati o chiesti da inserire all’utente. 


#3.1 calcolo mat inversa
def matrice_inversa():
    if matrice is None:
        print ("matrice inesistente")
    elif matrice.shape[0] != matrice.shape[1]:
        print ("matrice non quadrata")
    else:
        try:
            print("matrice inversa:\n", np.linalg.inv(matrice)) # linalg metodo calcolo inverso
        except:
            print("matrice non invertibile")

#3.2 applica funzione sin cas exp
def applica_funz():
    if matrice is None:
        print ("matrice inesistente")
        return
    
    funz = {"1": np.sin, "2": np.cos, "3": np.exp}
    nomi ={"1":"sin","2":"cos","3":"exp"}

    scelta = input("scegli funzione:\n 1-sin 2-cos 3-exp : ")

    if scelta in funz:
        print(f"{nomi[scelta]}(matrice):\n", funz[scelta](matrice))
    else:
        print("scelta non valida")

#3.3 filtro per condizione
def filtra_ele():
    if matrice is None:
       print("matrice inesistente")
       return
    try:
        soglia = float(input("inserisci valore: "))
        print(f"elementi maggiori di {soglia}:\n", matrice[matrice>soglia])
    except ValueError:
        print("valore non valido")


# MENU

def menu():
    while True:
        print("--------MENU--------")
        print("1. crea matrice 2d")
        print("2. estrai matrice")
        print("3. trasponi matrice")
        print("4. somma elementi")
        print("5. moltiplica elementi matrici")
        print("6. calcola media")
        print("7. matrice inversa")
        print("8. applica fuz sin, soc exp")
        print("9. filtra elementi magg")
        print("0. esci")
        
        scelta = input("opzione: ")

        if scelta == "1":
            crea_matrice()
        elif scelta == "2":
            sotto_matrice()
        elif scelta == "3":
            trasp_matrice()
        elif scelta == "4":
            somma_elementi()
        elif scelta == "5":
            moltip_elementwise()
        elif scelta == "6":
            media_matrice()
        elif scelta == "7":
            matrice_inversa()
        elif scelta == "8":
            applica_funz()
        elif scelta == "9":
            filtra_ele()
        elif scelta == "0":
            print("Uscita")
            break
        else:
            print("scelta non valida")

if __name__ == "__main__":
    menu()
