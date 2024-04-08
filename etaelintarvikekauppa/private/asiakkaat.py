import tuotteet

class Asiakas:
    
    def __init__(self, etunimi, sukunimi, osoite, postinumero, toimipaikka, sahkoposti, puhelinnumero):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.osoite = osoite
        self.postinumero = postinumero
        self.toimipaikka = toimipaikka
        self.sahkoposti = sahkoposti
        self.puhelinnumero = puhelinnumero
        self.kauppalista = []

    def lisaaListalle(self, tuote):
        self.kauppalista.append(tuote)

    def poistaListalta(self, tuote):
        self.kauppalista.remove(tuote)

    def getKauppalista(self):
        return self.kauppalista
    
    def __str__(self):
        return "[" + self.etunimi + " " + self.sukunimi + ", " + self.osoite + ", " + self.postinumero + ", " + self.toimipaikka + ", " + self.sahkoposti + ", " + self.puhelinnumero + "]"



def main():
    asiakas = Asiakas("Markus", "Frosti", "Ahomutka 7", "45360", "Valkeala", "admin@admin.fi", "0123456789")
    banaani = tuotteet.Banaani(14)
    omena = tuotteet.Omena(5)
    salaatti = tuotteet.Salaatti(6)
    asiakas.lisaaListalle(banaani)
    asiakas.lisaaListalle(omena)
    asiakas.lisaaListalle(salaatti)
    print(asiakas)
    print(banaani)

if __name__ == "__main__":
    main()