from database import get_connection

def ricerca_libri():
    criterio = input("Cerca per titolo o autore: ").strip()

    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        SELECT id, titolo, autore, disponibile 
        FROM libri 
        WHERE titolo LIKE %s OR autore LIKE %s
        """
        like_criterio = f"%{criterio}%"
        cursor.execute(query, (like_criterio, like_criterio))
        risultati = cursor.fetchall()

        if risultati:
            print(f"📚 Trovati {len(risultati)} risultati:")
            for libro in risultati:
                stato = "Disponibile" if libro[3] else "Non disponibile"
                print(f"ID: {libro[0]} | Titolo: {libro[1]} | Autore: {libro[2]} | Stato: {stato}")
        else:
            print("Nessun libro trovato con quel criterio.")
    except Exception as e:
        print(f"Errore nella ricerca: {e}")
    finally:
        conn.close()
