class Libro:

    def __init__(self, titolo, autore, pagine, editore):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        #self.casa_editrice = editore

    def descrizione(self):
        return f"il libro '{self.titolo}' di {self.autore} ha {self.pagine} pagine, la casa editrice {self.casa_editrice}"


libro1 = Libro("Il Signore degli Anelli", "Tolkien", 1178, "bellilibri")
libro2 = Libro("1984", "Orwell", 328, "")

Libro.casa_editrice = "Mondadori"

print(libro1.descrizione())
print(libro2.descrizione())