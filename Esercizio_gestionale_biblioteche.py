
## ESERCIZIO GESTIONALE BIBLIOTECHE: 

# Crea un gestionale per biblioteche, la
# biblioteca puoi inserire i libri (titolo,
# autore, stato prestito, id di chi l’ha
# preso in prestito), gli utenti possono
# cercare i libri per titolo e autore e
# prenderli in prestito se disponibile.


import  mysql, time, sys

myCursor = mydb.cursor()
 
sql = 'create database if not exists gestionale_biblioteche' 
myCursor.execute(sql)


sql = 'use gestionale_biblioteche'
myCursor.execute(sql)


sql_2 = 'create table if not exists utenti(ID_utente int AUTO_INCREMENT primary key, ' \
'Nome varchar(255) not null, Cognome varchar(255) not null, Admin bool default 0)' 
myCursor.execute(sql_2)
mydb.commit()


sql_1 = 'create table if not exists libri(ID_libro int AUTO_INCREMENT primary key, ' \
'Titolo varchar(255) not null, Autore varchar(255) not null, Stato_prestito bool default 0, ID_prestito int default null, ' \
'foreign key (ID_prestito) references utenti(ID_utente)) '
myCursor.execute(sql_1)
mydb.commit()

 
def crea_admin(): 
    val = ('admin', 'admin')

    sql = 'insert into utenti(nome,cognome, Admin) values (%s,%s, 1)'
    myCursor.execute(sql,val)
    mydb.commit()
    print(f'{val} registrato.')
    


def aggiungi_libri():
    finito = True
    while finito: 
        Titolo = input('Inserisci Titolo: ')
        Autore = input('Inserisci Autore: ')
        val = (Titolo.capitalize(), Autore.capitalize())

        result = controllo_libro(val)
        if result: 
            print('Libro già presente nella biblioteca.')
            dom = input('Aggiungere altro libro?\n1) Sì\n2) No\n>>')
            if dom == '2': finito = False
        else: 
            inserisci_libro(val)
            dom = input('Aggiungere altro libro?\n1) Sì\n 2) No\n>>')
            if dom == '2': finito = False


def controllo_libro(val): 
    check_libro = 'select ID_libro from libri where Titolo = %s and Autore = %s'
    myCursor.execute(check_libro, val)
    result = myCursor.fetchone()
    return result


def inserisci_libro(val): 
    sql = 'insert into libri(Titolo,Autore) values (%s,%s)'
    myCursor.execute(sql,val)
    mydb.commit()
    print(f'{val} inserito nella biblioteca.')


def elimina_libri():
    finito = True
    while finito: 
        Titolo = input('Inserisci Titolo: ')
        Autore = input('Inserisci Autore: ')
        val = (Titolo.capitalize(), Autore.capitalize())

        result = controllo_libro(val)
        if result: 
            rimuovi_libro(val)
            dom = input('Rimuovere altro libro?\n1) Sì\n 2) No\n')
            if dom == '2': finito = False
        else: 
            print('Libro NON presente nella biblioteca.')
            dom = input('Rimuovere altro libro?\n1) Sì\n 2) No\n')
            if dom == '2': finito = False


def rimuovi_libro(val): 
    sql = 'delete from libri where Titolo =  %s and Autore = %s'
    myCursor.execute(sql,val)
    mydb.commit()
    print(f'{val} rimosso dalla biblioteca.')


def aggiungi_utente():
    nome = input('Inserisci Nome: ')
    cognome = input('Inserisci Cognome: ')
    val = (nome.capitalize(), cognome.capitalize())

    result = controllo_utente(val)
    if result: 
        print('Utente già registrato.')
    else: 
        inserisci_utente(val)
        return val


def controllo_utente(val): 
    check_utente = 'select ID_utente from utenti where nome = %s and cognome = %s'
    myCursor.execute(check_utente, val)
    result = myCursor.fetchone()
    return result


def inserisci_utente(val): 
    sql = 'insert into utenti(nome,cognome) values (%s,%s)'
    myCursor.execute(sql,val)
    mydb.commit()
    print(f'{val} registrato.')


def elimina_utente():
    nome = input('Inserisci Nome: ')
    cognome = input('Inserisci Cognome: ')
    val = (nome.capitalize(), cognome.capitalize())

    result = controllo_utente(val)
    if result: 
        rimuovi_utente(val)
    else: 
        print('Utente NON registrato.')


def rimuovi_utente(val): 
    sql = 'delete from utenti where nome =  %s and cognome = %s'
    myCursor.execute(sql,val)
    mydb.commit()
    print(f'{val} rimosso.')


def visualizza_utenti() :
    sql = 'select * from utenti where Admin = 0'
    myCursor.execute(sql)
    myResult = myCursor.fetchall() # ho lista di tuple
    for risultato in myResult: 
        print(risultato)


def visualizza_libri() :
    sql = 'select * from libri'
    myCursor.execute(sql)
    myResult = myCursor.fetchall() # ho lista di tuple
    for risultato in myResult: 
        print(risultato)


def visualizza_libri_disponibili() :
    sql = 'select * from libri where Stato_prestito = 0'
    myCursor.execute(sql)
    myResult = myCursor.fetchall() # ho lista di tuple
    for risultato in myResult: 
        print(risultato)


def visualizza_libri_nondisp() :
    sql = 'select * from libri where Stato_prestito = 1'
    myCursor.execute(sql)
    myResult = myCursor.fetchall() # ho lista di tuple
    for risultato in myResult: 
        print(risultato)


def prestito(id_utente): #devo prendere dall'utente l'id_utente e l'id_libro
    while True: 
        visualizza_libri_disponibili()
        id_libro = input('Inserisci ID del libro da prendere in prestito\n>>')
        if id_libro.isdecimal(): 
            presta_libro(id_libro, id_utente)
            break
        else: print('Inserisci ID libro valido')


def presta_libro(id_libro, id_utente):
    sql = '''
    update libri 
    set Stato_prestito = 1, ID_prestito = %s 
    where ID_libro = %s and Stato_prestito = 0
    '''
    myCursor.execute(sql, (id_utente, id_libro))
    mydb.commit()

    if myCursor.rowcount == 0:
        print('Libro non disponibile o ID libro errato.')
    else:
        print('Libro preso in prestito.')


def restituzione(id_utente):
    while True: 
        visualizza_libri_nondisp()
        id_libro = input('Inserisci ID del libro da restituire\n>>')
        if id_libro.isdecimal(): 
            restituisci_libro(id_libro)
            break
        else: print('Inserisci ID libro valido')

def restituisci_libro(id_libro):
    sql = '''
    update libri 
    set Stato_prestito = 0, ID_prestito = NULL 
    where ID_libro = %s and Stato_prestito = 1
    '''
    myCursor.execute(sql, (id_libro,))
    mydb.commit()

    if myCursor.rowcount == 0:
        print('Libro già presente in libreria o ID libro errato.')
    else:
        print('Libro restituito.')


def cerca_libri(): 
    trovato = True
    while trovato: 
        inp = input('Vuoi cercare per:\n1) Titolo\n2) Autore\n>>')
        if inp == '1': 
            titolo = input('Inserisci titolo: ')
            sql_titolo = 'select * from libri where Titolo like %s'
            myCursor.execute(sql_titolo, (f"{titolo}%",))
            
        elif inp == '2': 
            autore = input('Inserisci autore: ')
            sql_autore= 'select * from libri where Autore like %s'
            myCursor.execute(sql_autore, (f"{autore}%",))
        
        else: print('Input errato')

        risultati = myCursor.fetchall()
        if risultati:
            trovato = False
            for r in risultati:
                print(r)
        else: print('Nessun risultato trovato.')

#########################################################################

def gestionale_biblioteche(): 
    sql_iniziale = "SELECT COUNT(*) FROM utenti"
    myCursor.execute(sql_iniziale)
    risultato = myCursor.fetchone()
    if risultato[0] == 0:
        print("La tabella utenti è vuota.\nCreazione utente admin di default in corso...")
        time.sleep(5)
        crea_admin()
        print("Riavvia per effettuare il login.")
        sys.exit()
        
    
    print('Benvenuto nel gestionale della biblioteca!')
    ingresso = input('1) Login\n2) Registrazione Utente\n>>')

    if ingresso == '1': 
        nome = input('Inserisci nome utente: ')
        cognome = input('Inserisci cognome utente: ')
        val = (nome, cognome)

    elif ingresso == '2': 
        val = aggiungi_utente()

    sel_id = 'select ID_utente, Admin from utenti where nome = %s and cognome = %s'
    myCursor.execute(sel_id, val)
    result = myCursor.fetchone()
    ID_user = result[0]
    Admin = result[1] # check se è admin

    if Admin == 1: 
        while True:
            print("\n--- MENU AMMINISTRATORE ---")
            print("1) Aggiungi Libro")
            print("2) Elimina Libro")
            print("3) Visualizza Utenti Registrati")
            print("4) Visualizza Tutti i Libri")
            print("5) Elimina Utente")
            print("6) Visualizza Libri Disponibili")
            print("7) Visualizza Libri in Prestito")
            print("8) Cerca Libri")
            print("9) Esci")

            scelta = input("Scegli un'opzione: ")

            if scelta == '1':
                aggiungi_libri()
            elif scelta == '2':
                elimina_libri()
            elif scelta == '3':
                visualizza_utenti()
            elif scelta == '4':
                visualizza_libri()
            elif scelta == '5':
                elimina_utente()
            elif scelta == '6':
                visualizza_libri_disponibili()
            elif scelta == '7':
                visualizza_libri_nondisp()
            elif scelta == '8':
                cerca_libri()
            elif scelta == '9':
                print("Uscita dal pannello amministratore.")
                break
            else:
                print("Scelta non valida. Riprova.")
    
    else:
        while True:
            print("\n--- MENU UTENTE ---")
            print("1) Visualizza Libri Disponibili")
            print("2) Cerca Libri")
            print("3) Prendi Libro in Prestito")
            print("4) Restituisci Libro")
            print("5) Esci")

            scelta = input("Scegli un'opzione: ")

            if scelta == '1':
                visualizza_libri_disponibili()
            elif scelta == '2':
                cerca_libri()
            elif scelta == '3':
                prestito(ID_user)
            elif scelta == '4':
                restituzione(ID_user)
            elif scelta == '5':
                print("Uscita dal gestionale.")
                break
            else:
                print("Scelta non valida. Riprova.")


############################# main

gestionale_biblioteche()
