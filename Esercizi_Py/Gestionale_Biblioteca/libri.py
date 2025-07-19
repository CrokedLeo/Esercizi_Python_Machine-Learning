from database import get_connection

def aggiungi_libro():
    titolo = input("Titolo del libro: ")
    autore = input("Autore del libro: ")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO libri (titolo, autore)
            VALUES (%s, %s)
        """, (titolo, autore))
        conn.commit()
        print("📚 Libro aggiunto con successo.")
    except Exception as e:
        print(f"❌ Errore durante l'inserimento: {e}")
    finally:
        conn.close()

def mostra_libri(mostra_solo_disponibili=False):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        if mostra_solo_disponibili:
            cursor.execute("SELECT * FROM libri WHERE disponibile = TRUE")
        else:
            cursor.execute("SELECT * FROM libri")

        libri = cursor.fetchall()
        if not libri:
            print("⚠️ Nessun libro trovato.")
        else:
            print("\n📚 LIBRI DISPONIBILI:")
            for libro in libri:
                stato = "✅ Disponibile" if libro["disponibile"] else "❌ Non disponibile"
                print(f"ID: {libro['id']} | Titolo: {libro['titolo']} | Autore: {libro['autore']} | {stato}")
    except Exception as e:
        print(f"❌ Errore nella lettura dei libri: {e}")
    finally:
        conn.close()
