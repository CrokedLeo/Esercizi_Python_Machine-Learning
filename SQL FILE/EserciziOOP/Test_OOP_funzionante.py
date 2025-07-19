from abc import ABC, abstractmethod
import random

#------classe astratta

class Soldato(ABC):
    def __init__(self, nome, costo, attacco,difesa, salute):    #inizializza
        self._nome=nome
        self._costo=costo
        self._attacco=attacco
        self._difesa=difesa
        self._salute=salute
        self._salute_massima=salute
        self._cooldown_abilita = 0  # turni prima di riutilizzare l abilità 
        self._effetti_attivi = {}  


    def difenditi(self, danno):
# funzione cavaliereplus        
        if hasattr(self, "_assorbi_danno") and self._assorbi_danno:  # restituisce True o False
            danno = danno // 2
            self._assorbi_danno = False
            print(f"{self._nome} con lo scudo para e riduce i danni a {danno}!")
# calcolo danno
        danno_effettivo=max(0, danno - self._difesa)
        self._salute -= danno_effettivo
        print(f"{self._nome} ha subito {danno_effettivo} danni!")

    def e_vivo(self):
        return self._salute>0

    def stato(self):
        indice_salute= self._salute/ self._salute_massima
        barra = "█" * int(20 * indice_salute) + "-" * (20 - int(20 * indice_salute))
        print(f"{self._nome} ({self.__class__.__name__}) | {self._salute}/{self._salute_massima} HP [{barra}]")

    def aggiorna_effetti(self):
        effetti_da_rimuovere = []
        for effetto, durata in self._effetti_attivi.items():
            if effetto == "avvelenato":
                danno = 5
                self._salute -= danno
                print(f"{self._nome} soffre per il veleno! Perde {danno} HP.")
            elif effetto == "benedetto":
                print(f"{self._nome} è benedetto e si sente rinvigorito.")

        # riduci durata effetto
            self._effetti_attivi[effetto] -= 1
            if self._effetti_attivi[effetto] <= 0:
                effetti_da_rimuovere.append(effetto)

        for effetto in effetti_da_rimuovere:
            print(f"{self._nome} non è più affetto da {effetto}.")
            del self._effetti_attivi[effetto]

    def turno_inizio(self):
        if self._cooldown_abilita > 0:
            self._cooldown_abilita -= 1
        self.aggiorna_effetti()

    @abstractmethod
    def attacca(self, avversario):#estratto per modifca
        pass

    @abstractmethod
    def usa_abilita_speciale(self, alleati=None, nemici=None):
        pass

#--------classi derivate
class Cavaliere(Soldato):
    def __init__(self, nome):
        super().__init__(nome, costo=250, attacco=30, difesa=20, salute=100)
        self._assorbi_danno = False
    def attacca(self, avversario):
        critico = random.random()<0.20
        danno= self._attacco * (2 if critico else 1)
        print(f"{self._nome} (Cavaliere) attacca con {'colpo critico' if critico else 'forza'}: {danno} danno")
        avversario.difenditi(danno)
# special
    def usa_abilita_speciale(self, alleati=None, nemici=None):
        self._assorbi_danno=True
        print(f"{self._nome} (Cavaliere) alza lo scudo! Prossimi danni dimezzati!")


class Arciere(Soldato):
    def __init__(self, nome):
        super().__init__(nome, costo=200, attacco=40, difesa=5, salute=60)

    def attacca(self, avversario):
        print(f"{self._nome} (Arciere) scocca una freccia: {self._attacco} danni")
        avversario.difenditi(self._attacco)
    
# special    
    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if nemici:
            print(f"{self._nome} (Arciere) scaglia piaggia di freccie!")
            for nemico in nemici:
                if nemico.e_vivo():
                    danno = self._attacco // 2
                    print(f"Colpisce {nemico._nome} per {danno} danni")
                    nemico.difenditi(danno)


class Guaritore(Soldato):
    def __init__(self, nome):
        super().__init__(nome, costo=180, attacco=10, difesa=5, salute=70)
        self._resurrezione_usata = False

    def attacca(self, avversario=None, alleati=None):
        if alleati:
            vivi = [s for s in alleati if s != self and s.e_vivo()]
            if vivi:
                target = random.choice(vivi)
                cura = 30
                target._salute = min(target._salute + cura, target._salute_massima)
                print(f"{self._nome} (Guaritore) cura {target._nome} di {cura} HP")
            else:
                print(f"{self._nome} nessuno da curare.")
        else:
            print(f"{self._nome} non ci sono alleati da curare.")

#special
    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if self._resurrezione_usata:
            print(f"{self._nome} ha già usato il potere di resurrezione.")
            return
        morti = [s for s in alleati if s != self and not s.e_vivo()]
        if morti:
            resuscitato = morti[0]
            resuscitato._salute = resuscitato._salute_massima // 2
            self._resurrezione_usata = True
            print(f"{self._nome} (Guaritore) rianima {resuscitato._nome} con {resuscitato._salute} HP!")
            alleati.append(resuscitato)
        else:
            print(f"{self._nome} non ha nessuno da rianimare.")


class Mago(Soldato):
    def __init__(self, nome):
        super().__init__(nome, costo=300, attacco=0, difesa=5, salute=65)

    def attacca(self, avversario):
        if random.random() < 0.25:
            print(f"{self._nome} (Mago) è troppo stanco si addormenta!")
            return
        danno = random.randint(10, 40)
        print(f"{self._nome} (Mago) lancia un incantesimo: {danno} danni")
        avversario.difenditi(danno)
# special
    def usa_abilita_speciale(self, alleati=None, nemici=None):
        golem = Golem()
        alleati.append(golem)
        print(f"{self._nome} (Mago) evoca un Golem temporaneo!")



class Golem(Soldato):
    def __init__(self, nome ="golem", durata=3):
        super().__init__("Golem", costo=0, attacco=50, difesa=0, salute=100)
        self._temporaneo = True
        self._durata = durata
        
    def attacca(self, avversario):
        print("il Golem attacca con furia!")
        avversario.difenditi(self._attacco)

    def aggiorna_turno(self):
        self._durata -= 1
        if self._durata <= 0:
            print(f"{self._nome} si dissolve, durata finita!")
            return True  # indica che deve essere rimosso
        return False

    def difenditi(self, danno):
        danno_effettivo = max(0, danno - self._difesa)
        self._salute -= danno_effettivo
        if self._salute <= 0:
            print(f"{self._nome} è stato distrutto!")
            return True
        return False

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        print(f"{self._nome} non usa abilità speciale.")
        pass

#------classe extra
class Assassino(Soldato):
    def __init__(self, nome):
        super().__init__(nome, costo=220, attacco=35, difesa=10, salute=75)

    def attacca(self, avversario):
        print(f"{self._nome} (Assassino) attacca con lama silenziosa: {self._attacco} danni")
        avversario.difenditi(self._attacco)

    def usa_abilita_speciale(self, alleati=None, nemici=None):
        if self._cooldown_abilita > 0:
            print(f"{self._nome} non può ancora usare la sua abilità! ({self._cooldown_abilita} turni restanti)")
            return
        if nemici:
            target = random.choice([n for n in nemici if n.e_vivo()])
            target._effetti_attivi["avvelenato"] = 3  # 3 turni
            self._cooldown_abilita = 2  # 2 turni di attesa
            print(f"{self._nome} (Assassino) avvelena {target._nome}! Perderà HP ogni turno.")

#--------funzioni gioco

def crea_soldato(tipo, nome):
    if tipo == "cavaliere":
        return Cavaliere(nome)
    elif tipo == "arciere":
        return Arciere(nome)
    elif tipo == "guaritore":
        return Guaritore(nome)
    elif tipo == "mago":
        return Mago(nome)
    elif tipo == "assassino":
        return Assassino(nome)
    else:
        print("Tipo non valido.")
        return None


def acquista_esercito(budget):
    esercito= []
    while True:
        print(f"\nBudget restante: {budget}")
        print("Classi: Cavaliere (250), arciere (200), guaritore (180), mago(300), assassino(220)")
        tipo= input ("Scegli classe o 'fine': ").lower()
        if tipo == "fine":
            break
        nome = input("Dai nome in codice all'unita:")
        soldato= crea_soldato (tipo, nome)

        if soldato and budget >= soldato._costo:
            esercito.append(soldato)
            budget -= soldato._costo

        else:
            print("Il tuo regno è povero!")
    return esercito, budget

#----skynet

def skynet_acquisto(budget):
    tipi =[Cavaliere, Arciere, Guaritore, Mago, Assassino]
    esercito = []
    print("\n Skynet compra rinforzi...")

    while budget >=180:
        cls = random.choice(tipi)
        soldato= cls(f"Skynet_{cls.__name__}_{len(esercito)}")
        
        if budget >= soldato._costo:
            esercito.append(soldato)
            budget-= soldato._costo
            print(f"Skynet ha reclutato {cls.__name__}")
    return esercito, budget

#------combattimento

def scontro_round(esercito_gio, esercito_sky):
    print("\n--Schermaglia--")
 
    for s in esercito_gio + esercito_sky:
        s.turno_inizio()
 #------rimuovi golem       
    for s in esercito_gio[:]:
        if isinstance(s, Golem):
            if s.aggiorna_turno():
                esercito_gio.remove(s)
                print(f"{s._nome} rimosso dall'esercito del giocatore.")

    for s in esercito_sky[:]:
        if isinstance(s, Golem):
            if s.aggiorna_turno():
                esercito_sky.remove(s)
                print(f"{s._nome} rimosso dall'esercito di Skynet.")


# gicatore usa abilita
    for soldato in esercito_gio:
        if not isinstance(soldato,Golem):
            usa = input(f"Vuoi usare abilità speciale di {soldato._nome}? (s/n): ").lower()
            if usa == "s":
                soldato.usa_abilita_speciale(alleati=esercito_gio, nemici =esercito_sky)

# skynet abilità random
    for soldato in esercito_sky:
        if soldato.e_vivo() and random.random() <0.3:
            soldato.usa_abilita_speciale(alleati=esercito_sky, nemici=esercito_gio)

# 1v1
    for s1, s2 in zip(esercito_gio, esercito_sky):
        if s1.e_vivo() and s2.e_vivo():
            if isinstance(s1,Guaritore):
                s1.attacca(alleati = esercito_gio)
            else:
                s1.attacca(s2)
            if s2.e_vivo():
                if isinstance(s2, Guaritore):
                    s2.attacca(alleati = esercito_sky)
                else:
                    s2.attacca(s1)
# togli morti
    esercito_gio[:]=[s for s in esercito_gio if s.e_vivo()]   
    esercito_sky[:]=[s for s in esercito_sky if s.e_vivo()]

# stato dell esercito
    print("\n--Stato Esercito Giocatore--")
    for s in esercito_gio:
        s.stato()

    print("\n--Stato Esercito Skynet--")
    for s in esercito_sky:
        s.stato()


#-------main

def main():
    budget_gio= budget_sky = 1000
    esercito_gio, budget_gio = acquista_esercito(budget_gio)
    esercito_sky, budget_sky = skynet_acquisto(budget_sky)

    round_num = 0
    while esercito_gio and esercito_sky:
        round_num +=1
        scontro_round(esercito_gio, esercito_sky)

        if not esercito_gio or not esercito_sky:
            break

        print("\nFine dello sconto! Ogni fazione riceve +300 dobloni")
        budget_gio += 300
        budget_sky += 300

        nuovo_esercito_gio, nuovo_budget_gio = acquista_esercito(budget_gio)
        esercito_gio.extend(nuovo_esercito_gio)
        budget_gio = nuovo_budget_gio

        nuovo_esercito_sky, nuovo_budget_sky = skynet_acquisto(budget_sky)
        esercito_sky.extend(nuovo_esercito_sky)
        budget_sky = nuovo_budget_sky

    print("\n-Fine della Guerra-")
    vincitore= "Giocatore" if esercito_gio else "SkyNet"
    
    print(f"Vittoria di: {vincitore}")
    print(f"Schermaglie avvenute: {round_num}")
    print(f"Soldati sopravvisuti nel regnio: {len(esercito_gio)}")
    print(f"Soldati sopravvisuti di Skynet: {len(esercito_sky)}")

if __name__ == "__main__":
    main()