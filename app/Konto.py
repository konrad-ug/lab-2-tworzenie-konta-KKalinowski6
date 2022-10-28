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

    def Przelew_przychodzacy(self, wartosc):
        self.saldo += wartosc

    def Przelew_wychodzacy(self, wartosc):
        if (self.saldo - wartosc >= 0):
            self.saldo -= wartosc

    def Ekspresowy_przelew_wychodzacy(self, wartosc):
        if(self.saldo - wartosc - self.Nalicznie_oplaty_za_przelew_ekspresowy() >= 0):
            self.saldo -= wartosc + self.Nalicznie_oplaty_za_przelew_ekspresowy()

    def Nalicznie_oplaty_za_przelew_ekspresowy(self):
        return 1

class Konto_Firmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.Sprawdzanie_NIP(nip)
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
    
    def Sprawdzanie_NIP(self, nip):
        if (len(nip) == 10):
            self.nip =  nip
        else:
            self.nip =  "Niepoprawny NIP!" 

    def Nalicznie_oplaty_za_przelew_ekspresowy(self):
        return 5