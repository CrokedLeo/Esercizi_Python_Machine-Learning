import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # Cambia se hai user diverso
    "password": "",          # Cambia se hai password diversa
}

DB_NAME = "biblioteca"

def crea_database_e_tabelle():
    try:
        # Connessione iniziale (senza DB)
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.close()

        # Riconnessione con il database specificato
        conn = mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
        cursor = conn.cursor()

        # Creazione tabella utenti
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS utenti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        """)

        # Creazione tabella libri
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libri (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titolo VARCHAR(200) NOT NULL,
                autore VARCHAR(100) NOT NULL,
                disponibile BOOLEAN DEFAULT TRUE
            )
        """)

        # Creazione tabella prestiti
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestiti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                utente_id INT,
                libro_id INT,
                data_prestito DATE,
                data_restituzione DATE,
                FOREIGN KEY (utente_id) REFERENCES utenti(id),
                FOREIGN KEY (libro_id) REFERENCES libri(id)
            )
        """)

        conn.commit()
        conn.close()
    except mysql.connector.Error as e:
        print(f"Errore nella connessione al database: {e}")
        exit(1)

def get_connection():
    try:
        return mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"Errore nella connessione al database: {e}")
        exit(1)
