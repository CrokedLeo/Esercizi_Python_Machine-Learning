from abc import ABC, abstractmethod
import random
import time

#----------scrive log
def log(testo):
    with open("log_torneo.txt", "a", encoding="utf-8") as file: 
       file.write(testo + "\n")

#--------------classe 
class Combattente(ABC):
    def __init__(self, nome, salute, attacco_base, difesa_base):
        self._nome=nome
        self._salute=salute
        self._salute_massima = salute
        self._attacco_base= attacco_base
        self._difesa_base= difesa_base

    @abstractmethod
    def attacca (self, avversario):
        pass

    def subisci_danno(self, danno):
        danno_effettivo = max(0, danno - self._difesa_base)
        self._salute -= danno_effettivo
        print(f"{self._nome} riceve {danno_effettivo} danni (HP rimasti: {self._salute}) ")

    def vivo(self):
        return self._salute > 0
    

    """def stato(self):
        barra_salute = "█" * (self._salute // 10)
        print(f"{self._nome} - salute: {self._salute} {barra_salute}")"""
    
    def stato(self):
        lunghezza_barra = 20
        salute_indice = self._salute / self._salute_massima
        blocchi = int(lunghezza_barra * salute_indice)
        barra_salute = "█" * blocchi + "-" * (lunghezza_barra - blocchi)
        print(f"{self._nome} - salute: {self._salute}/{self._salute_massima} [{barra_salute}]")


    def rigenera_salute(self):
        recupero = random.randint(10, 20)
        self._salute = min(self._salute + recupero, self._salute_massima)
        print(f"Vince {self._nome} e recupera {recupero} HP!!!(HP Totali: {self._salute})")


    def get_nome(self):
        return self._nome

    def get_tipo(self):
        return self.__class__.__name__


#--------------------------------------------------------------


class Cavaliere(Combattente):
    def __init__(self, nome):
        super().__init__(nome, salute=120, attacco_base=25, difesa_base=10)


    def attacca(self, avversario):
        danno = self._attacco_base
        if random.random() < 0.2:
            danno += 2
            print(f"{self._nome} ha crittato!!!!")
        else:
            print(f"{self._nome} attacca di spadone!")
        avversario.subisci_danno(danno)



class Arciere(Combattente):
    def __init__(self, nome):
        super().__init__(nome, salute=100, attacco_base=20, difesa_base=5)


    def attacca(self, avversario):
            print(f"{self._nome} scocca fraccia!!!")
            avversario.subisci_danno(self._attacco_base)
            if random.random() < 0.3:
                print(f"{self._nome} fa doppio attacco!!")
                avversario.subisci_danno(self._attacco_base)



class Mago(Combattente):
    def __init__(self, nome):
        super().__init__(nome, salute=90, attacco_base=0, difesa_base=3)

    def attacca(self, avversario):
        danno = random.randint(10,50)
        print (f"{self._nome} lancia incantesimo che fa {danno} di danno!!")
        avversario.subisci_danno(danno)


#-------------------------------------

def cera_partecipanti():
    partecipanti= []
    n = int(input("quanti giocatori siete? "))
    
    for i in range(n):
        while True:
            tipo = input(f"Combattente n-{i+1} - Tipo (cavaliere/arciere/mago): ").lower()
            nome = input("Nome: ")
        
            if tipo == "cavaliere":
                partecipanti.append(Cavaliere(nome))
                break

            elif tipo == "arciere":
                partecipanti.append(Arciere(nome))
                break

            elif tipo == "mago":
                partecipanti.append(Mago(nome))
                break

            else:
                print("giocatore non esiste")
            continue
    return partecipanti



def combattimento(c1, c2):

    print(f"Fight! {c1.get_nome()} VS {c2.get_nome()} ")
    log(f"Fight! {c1.get_nome()} VS {c2.get_nome()} - ")
    time.sleep(3)

    turno = 0 
    while c1.vivo() and c2.vivo():
        turno +=1
        print (f"# {turno} #")
        time.sleep(2)

        c1.stato()
        c2.stato()
        time.sleep(1)


        if random.choice([True, False]):
            print(f"\n{c1.get_nome()} attacca {c2.get_nome()}:")
            time.sleep(1)

            c1.attacca(c2)
            time.sleep(2)

            if c2.vivo():
                print(f"\n{c2.get_nome()} attacca {c1.get_nome()}:")
                time.sleep(1)
                c2.attacca(c1)
                time.sleep(2)

        
        else:
            print(f"\n{c2.get_nome()} attacca {c1.get_nome()}:")
            time.sleep(1)

            c2.attacca(c1)
            time.sleep(2)

            if c1.vivo():
                print(f"\n{c1.get_nome()} attacca {c2.get_nome()}:")
                time.sleep(1)

                c1.attacca(c2) 
                time.sleep(2)

    vincitore = c1 if c1.vivo() else c2
    print(f" Ha vinto {vincitore.get_nome()}!!!")
    log(f" Ha vinto {vincitore.get_nome()}!")

    time.sleep(3)

    vincitore.rigenera_salute()
    time.sleep(1)

    return vincitore



def torneo(partecipanti):
    round_num = 1
    
    while len(partecipanti)>1:
        print(f" Round N-{round_num}")
        time.sleep(2)

        random.shuffle(partecipanti)
        
        vincitori = []
        for i in range(0, len(partecipanti), 2):
            
            if i+1 >= len(partecipanti):
                print(f"{partecipanti[i].get_nome()} vince a tavolino!")
                log(f"{partecipanti[i].get_nome()} vince a tavolino!")
                
                time.sleep(2)

                vincitori.append(partecipanti[i])
            
            else:
                vincitore = combattimento(partecipanti[i], partecipanti[i+1])
                vincitori.append(vincitore)
        partecipanti = vincitori
        round_num += 1

    print(f"\n SEI IL CAMPIONE {partecipanti[0].get_nome()}!!!!!!")
    log(f"\n IL CAMPIONE E {partecipanti[0].get_nome()} MIGLIOR {partecipanti[0].get_tipo()}!")
    time.sleep(3)

#------------------------------------------------------------------

def main(): 
    print(" RANDOMach! \n Random fight game! ")
    time.sleep(2)


    partecipanti = cera_partecipanti()
    if len(partecipanti) < 2:
        print ("dei essere in due per combattere")
        return
    torneo(partecipanti)

if __name__ == "__main__":
    main()