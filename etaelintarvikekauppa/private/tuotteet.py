class Tuote:
    def __init__(self,maara):
        self.maara = maara


class Banaani(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Banaani"
        self.kilohinta = 2.50

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"

class Kaali(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Kaali"
        self.kilohinta = 4.00

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"

class Kurkku(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Kurkku"
        self.kilohinta = 2.80

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"
        
class Mandariini(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Mandariini"
        self.kilohinta = 2.30

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"
        
class Omena(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Omena"
        self.kilohinta = 4.20

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"
        
class Porkkana(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Porkkana"
        self.kilohinta = 1.90

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"
        
class Persimon(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Persimon"
        self.kilohinta = 2.25

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"
        
class Salaatti(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Salaatti"
        self.kilohinta = 3.65

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"
        
class Tomaatti(Tuote):
    def __init__(self, maara):
        super().__init__(maara)
        self.nimi = "Tomaatti"
        self.kilohinta = 2.15

    def getKokoHinta(self):
        return self.maara*self.kilohinta
    
    def __str__(self):
        return "[" + self.nimi + ", määrä " + str(self.maara) + " kappaletta, hinta " + str(self.kilohinta) + "€ per kilo" + "]"

def main():
    tomaatti = Tomaatti(25)
    print(tomaatti)

if __name__ == "__main__":
    main()