import mysql.connector

connector = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ll280693!",
    database=""
)

myCursor = connector.cursor()

# creare un nuovo database
myCursor.execute("CREATE DATABASE IF NOT EXISTS esercizioDB")   

# selezionare il database appena creato
connector.database = "esercizioDB"

# creare una tabella
myCursor.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cognome VARCHAR(100)
)
""")

#myCursor.execute("CREATE TABLE IF NOT EXISTS utenti"
#"(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100),"
#"cognome VARCHAR(100))")


# inserire valori nella tabella
dati = [
    ("Mario", "Rossi"),
    ("Luigi", "Verdi"),
    ("Anna", "Bianchi")
]

myCursor.executemany("INSERT INTO utenti (nome, cognome) VALUES (%s, %s)", dati)
connector.commit()

# visualizzare i dati inseriti
myCursor.execute("SELECT * FROM utenti")
risultati = myCursor.fetchall()
for risultato in risultati:
    print(risultato)

# chiudere il cursore e la connessione
myCursor.close()
connector.close()

