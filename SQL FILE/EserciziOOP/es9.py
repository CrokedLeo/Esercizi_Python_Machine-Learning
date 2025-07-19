
class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila= fila
        self._occupato = False

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"posto{self._fila}{self._numero} prenotato")
        else:
            print("posto occupato")
    
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"posto {self._fila}{self._numero} ora libero")
        else:
            print(f"posto {self._fila}{self._numero} gia libero")

    def get_numero(self):
        return self._numero
    
    def get_fila(self):
        return self._fila
    
    def is_occupato(self):
        stato = "occupato" if self._occupato else "libero"
        return f"posto {self._fila}{self._numero}, {stato}"
    

# VIP

class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero,fila)
        self._servizi_extra = servizi_extra

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"posto VIP {self._fila}{self._numero} prenotato con {self._servizi_extra}")
        else:
            print(f"posto VIP {self._fila}{self._numero} prenotato")

    def __str__(self):
        stato = "occupato" if self._occupato else "libero"
        return f"posto {self._fila}{self._numero}, {stato}"

# standard

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_servizi = 2):
        super().__init__(numero, fila)
        self._costo_servizi = costo_servizi

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"posto standard {self._fila}{self._numero} prenotato con costo extra: {self._costo_servizi}")
        else:
            print(f"posto standard {self._fila}{self._numero} prenotato")

    def __str__(self):
        stato = "occupato" if self._occupato else "libero"
        return f"posto {self._fila}{self._numero}, {stato} con costo extra {self._costo_servizi}"


# teatro

class Teatro:
    def __init__(self):
        self._posti = []

    def aggiungi_posto(self, posto):
        self._posti.append(posto)

    def prenota_posto(self, numero, fila):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                return
    print("Posto non trovato")

    def stampa_posti_occupati(self):
        print("posti occupati:")
        for posto in self._posti:
            if posto.is_occupato():
                print(posto)


#------main

def main():
    teatro = Teatro()

    # Aggiunta di posti
    teatro.aggiungi_posto(PostoStandard(1, 'A'))
    teatro.aggiungi_posto(PostoStandard(2, 'A'))
    teatro.aggiungi_posto(PostoVIP(1, 'B', servizi_extra="Accesso lounge"))
    teatro.aggiungi_posto(PostoVIP(2, 'B', servizi_extra="Servizio al posto"))

    # Prenotazioni
    teatro.prenota_posto(1, 'A')
    teatro.prenota_posto(1, 'B')
    teatro.prenota_posto(3, 'C')  # inesistente

    # Stampa posti occupati
    teatro.stampa_posti_occupati()

if __name__ == "__main__":
    main()