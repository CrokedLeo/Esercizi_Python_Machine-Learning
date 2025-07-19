
import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database_name):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        self.database_name = database_name
        self.init_database()

    def init_database(self):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
        self.cursor.execute(f"USE {self.database_name}")
    

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS studenti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS voti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                studente_id INT,
                materia_id ENUM('Italiano', 'Matematica'),
                voto FLOAT,
                FOREIGN KEY (studente_id) REFERENCES studenti(id)
            )
        """)

    def inserisci_studente(self, nome,):
        self.cursor.execute("""
            INSERT INTO studenti (nome)
            VALUES (%s)
        """, (nome ))
        self.conn.commit()

    def inserisci_voto(self, id_studente, voto, materia):
        self.cursor.execute("""
            UPDATE voti
            SET voto = %s, materia = %s
            WHERE id = %s
        """, (voto, materia, id_studente))
        self.conn.commit()

    def visualizza_studenti(self):
        self.cursor.execute("SELECT id, nome FROM studenti")
        return self.cursor.fetchall()

    def modifica_studente(self, nuovo_nome):
        self.cursor.execute("""
            UPDATE studenti
            SET nome = %s
            WHERE id = %s
        """, (nuovo_nome))
        self.conn.commit()
#
    def elimina_studente(self, id_studente):
        self.cursor.execute("DELETE FROM studenti WHERE id = %s", (id_studente,))
        self.conn.commit()

    def chiudi_connessione(self):
        self.cursor.close()
        self.conn.close()
