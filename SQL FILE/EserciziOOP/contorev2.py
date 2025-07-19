class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        self.__titolare = None
        self.__saldo = 0
        
        self.set_titolare(titolare)
        if saldo_iniziale >= 0:
            self.__saldo = float(saldo_iniziale)

    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare.strip()
        else:
            print("Errore: il titolare deve essere una stringa non vuota.")



    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo:.2f} effettuato.")
        else:
            print("Errore: l'importo da depositare deve essere positivo.")




    def preleva(self, importo):
        if importo <= 0:
            print("Errore: inserire un importo positivo.")
        elif importo > self.__saldo:
            print("Errore: saldo insufficiente.")
        else:
            self.__saldo -= importo
            print(f"Prelievo di {importo:.2f} effettuato.")



    def visualizza_saldo(self):
        return self.__saldo

    def __str__(self):
        return f"Titolare: {self.__titolare}, Saldo: {self.__saldo:.2f} "




#---------main

def main():
    conto = ContoBancario("Mario Rossi", 100.0)
    print(conto)

    conto.deposita(50)
    conto.preleva(30)
    print(f"Saldo attuale: {conto.visualizza_saldo():.2f}")

    conto.set_titolare("Luigi Verdi")
    print(f"Nuovo titolare: {conto.get_titolare()}")

    conto.deposita(-10)  # Errore
    conto.preleva(500)   # Errore: saldo insufficiente

if __name__ == "__main__":
    main()
