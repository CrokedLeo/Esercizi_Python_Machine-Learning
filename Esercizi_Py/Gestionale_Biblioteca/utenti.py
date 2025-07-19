from database import get_connection

def aggiungi_utente():
    nome = input("Nome utente: ")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO utenti (nome)
            VALUES (%s)
        """, (nome,))
        conn.commit()
        print("👤 Utente aggiunto con successo.")
    except Exception as e:
        print(f"❌ Errore durante l'inserimento: {e}")
    finally:
        conn.close()

def mostra_utenti():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM utenti")
        utenti = cursor.fetchall()
        if not utenti:
            print("⚠️ Nessun utente registrato.")
        else:
            print("\n👥 UTENTI REGISTRATI:")
            for utente in utenti:
                print(f"ID: {utente['id']} | Nome: {utente['nome']}")
    except Exception as e:
        print(f"❌ Errore nella lettura degli utenti: {e}")
    finally:
        conn.close()
