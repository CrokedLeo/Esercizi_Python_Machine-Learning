import random
from abc import ABC, abstractmethod


class MetodoPagamento(ABC):
    @abstractmethod
    def effettua_pagamento(self, importo):
        print(f"[Generico] Pagamento di euro {importo}")
        pass



class CartaDiCredito(MetodoPagamento):
    def __init__(self, numero_carta, titolare):
        self.numero_carta = numero_carta
        self.titolare = titolare

    def effettua_pagamento(self, importo):
        print(f"[Carta] euro {importo} addebitati a {self.titolare} ({self.numero_carta})")





class PayPal(MetodoPagamento):
    def __init__(self, email):
        self.email = email

    def effettua_pagamento(self, importo):
        print(f"[PayPal] euro {importo} pagati con account {self.email}")




class BonificoBancario(MetodoPagamento):
    def __init__(self, iban, int):
        self.iban = iban
        self.int = int

    def effettua_pagamento(self, importo):
        print(f"[Bonifico] euro {importo} a {self.int} 'IBAN: {self.iban}")





class GestorePaga:
    def __init__(self):
        self._metodi= []

    def aggiungi_metodo(self, metodo):
        self._metodi.append(metodo)

    def effettua_pagacaso(self, importo):
        if not self._metodi:
            print("non disponibile")
            return
        metodo = random.choice(self._metodi)
        print("paga a caso:")
        metodo.effettua_pagamento(importo)




#-------main------
def main():
    carta = CartaDiCredito("1234567890123456", "Mario")
    paypal = PayPal("mario@example.com")
    bonifico = BonificoBancario("IT60X0542811101000000123456", "Mario Rossi")

    gestore = GestorePaga()
    gestore.aggiungi_metodo(carta)
    gestore.aggiungi_metodo(paypal)
    gestore.aggiungi_metodo(bonifico)

    for i in range(5):
        print(f"\nPagamento #{i+1}")
        gestore.effettua_pagacaso(random.randint(10, 100))

if __name__ == "__main__":
    main()
 