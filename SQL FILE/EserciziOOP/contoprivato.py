class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        self.__titolare = None
        self.__slado = 0
        self.set_tiolare(titolare)
        if saldo_iniziale >= 0:
            self.__saldo = float(saldo_iniziale)


def get_titolare(self):
    return self.__titolare

def set_titolare(self, nuovo_titolare):
    if isinstance(nuovo_titolare,str) and nuovo_titolare.strip():
        self.__titolare= nuovo_titolare.strip()
    else:
        print("errore deve essere una stringa vuota")

def deposita(self, importo):

    if importo > 0:
        self.__saldo += importo
        print(f"deposito {importo} effettuato")
    else:
        print("errore importo negativo")


def preleva(self, importo):
    if importo <=0:
        print ("inserire importo positivo")
    
    elif importo > self.__saldo:
        print("saldo insufficiente")

    else:
        self.__saldo -= importo
        print(f"prelievo di {importo} effettuato")

def visualizza_saldo(self):
    return self.__saldo

def __str__(self):
    return f"titolare{self.__titolare}, saldo: {self.__saldo}"

#---------main


def main():

    conto = ContoBancario("Mario Rossi", 100.0)

    print(conto) 

    conto.deposita(50)
    conto.preleva(30)
    print(f"Saldo attuale: {conto.visualizza_saldo():.2f}")

    conto.set_titolare("Luigi Verdi")
    print(conto.get_titolare())  

    conto.deposita(-10)  # Errore
    conto.preleva(500)   # Errore: saldo insufficiente


if __name__ == "__main__":
    main()
