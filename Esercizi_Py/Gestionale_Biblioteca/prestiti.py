from database import get_connection

def effettua_prestito():
    try:
        libro_id = int(input("ID del libro da prendere in prestito: "))
        utente_id = int(input("ID dell'utente che prende in prestito: "))
    except ValueError:
        print("⚠️ Inserisci solo numeri validi per ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Verifica che il libro esista e sia disponibile
        cursor.execute("SELECT disponibile FROM libri WHERE id = %s", (libro_id,))
        libro = cursor.fetchone()
        if not libro:
            print("❌ Libro non trovato.")
            return
        if libro[0] == 0:
            print("⚠️ Il libro non è disponibile.")
            return

        # Verifica che l'utente esista
        cursor.execute("SELECT id FROM utenti WHERE id = %s", (utente_id,))
        if not cursor.fetchone():
            print("❌ Utente non trovato.")
            return

        # Esegui il prestito
        cursor.execute("""
            INSERT INTO prestiti (id_libro, id_utente)
            VALUES (%s, %s)
        """, (libro_id, utente_id))
        cursor.execute("UPDATE libri SET disponibile = 0 WHERE id = %s", (libro_id,))
        conn.commit()
        print("📚 Prestito registrato con successo.")
    except Exception as e:
        print(f"❌ Errore durante il prestito: {e}")
    finally:
        conn.close()

def restituisci_libro():
    try:
        libro_id = int(input("ID del libro da restituire: "))
    except ValueError:
        print("⚠️ Inserisci un numero valido.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Verifica se il libro è stato prestato
        cursor.execute("""
            SELECT id FROM prestiti
            WHERE id_libro = %s AND data_restituzione IS NULL
        """, (libro_id,))
        prestito = cursor.fetchone()
        if not prestito:
            print("⚠️ Nessun prestito attivo trovato per questo libro.")
            return

        # Registra la restituzione
        cursor.execute("""
            UPDATE prestiti
            SET data_restituzione = NOW()
            WHERE id = %s
        """, (prestito[0],))
        cursor.execute("UPDATE libri SET disponibile = 1 WHERE id = %s", (libro_id,))
        conn.commit()
        print("✅ Libro restituito correttamente.")
    except Exception as e:
        print(f"❌ Errore durante la restituzione: {e}")
    finally:
        conn.close()
