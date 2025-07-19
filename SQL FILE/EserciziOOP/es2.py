import math

class Punto:  # dichiaro la classe

    def __init__(self, x, y):  # costruttore
        self.x = x 
        self.y = y 

    def muovi(self, dx, dy): 
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)

# creo due oggetti della classe Punto
punto1 = Punto(3, 4)
punto2 = Punto(0, 0)


punto1.muovi(2, 6)
punto2.muovi(2, 7)

print("Distanza di punto1:", punto1.distanza_da_origine())
print("Distanza di punto2:", punto2.distanza_da_origine())
