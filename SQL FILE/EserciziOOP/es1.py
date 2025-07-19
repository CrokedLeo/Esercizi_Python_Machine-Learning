class Punto:  

    def __init__(self, x, y):
        self.x = x  
        self.y = y  

    def muovi(self, dx, dy):  
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):  
        return (self.x ** 2 + self.y ** 2) ** 0.5  

# creo due oggetti Punto
punto1 = Punto(3, 4)
punto2 = Punto(0, 0)

# muovo il primo punto
punto1.muovi(1, 2)

# stampo le distanze
print("Distanza di punto1 dall'origine:", punto1.distanza_da_origine())
print("Distanza di punto2 dall'origine:", punto2.distanza_da_origine())
