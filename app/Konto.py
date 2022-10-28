class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy = None):
        if (len(pesel) == 11):
            self.imie = imie
            self.nazwisko = nazwisko
            self.pesel = pesel
            self.kod_rabatowy = kod_rabatowy
            self.saldo = self.Naliczanie_promocji()
        else:
            self.error = "Error"
        
    def Naliczanie_promocji(konto):
        if (konto.kod_rabatowy == "PROM_XYZ" and (int(konto.pesel[0:2]) > 60 or int(konto.pesel[2]) > 1)):
            return 50
        else:
            return 0
        pass
