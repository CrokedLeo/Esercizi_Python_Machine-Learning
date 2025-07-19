class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def verso(self):
        return "Suono"

class Leone(Animale):
    def __init__(self, nome, eta, criniera):
        super().__init__(nome, eta)
        self.criniera = criniera

    def verso(self):
        return "Roar"

    def sonno(self):
        return f"{self.nome} sta dormendo"

class Elefante(Animale):
    def __init__(self, nome, eta, peso):
        super().__init__(nome, eta)
        self.peso = peso

    def verso(self):
        return "Pruuuu"

    def spruzza_acqua(self):
        return f"{self.nome} spruzza acqua"





class Zoo:
    def __init__(self):
        self.animali = []

    def aggiungi(self, animale):
        self.animali.append(animale)

    def mostra(self):
        for a in self.animali:
            print(f"{a.nome}, Età: {a.eta}, Suono: {a.verso()}")
            
            if isinstance(a, Leone):
                print(" ", a.sonno())
            
            elif isinstance(a, Elefante):
                print(" ", a.spruzza_acqua())




zoo = Zoo()

zoo.aggiungi(Leone("fifone", 4, criniera=True))
zoo.aggiungi(Elefante("bro", 8, peso=1200))

zoo.mostra()
