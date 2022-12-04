class RejestrKont:
    list = []

    @classmethod
    def Dodaj_konto(cls, konto):
        cls.list.append(konto)

    @classmethod
    def Ile_kont(cls):
        return len(cls.list)

    @classmethod
    def Wyszukaj_konto_peselem(cls, pesel):
        for i in cls.list:
            if i.pesel == pesel:
                return i 
        return None

    @classmethod
    def Zmien_wartosci_konta(cls, pesel, imie="", nazwisko="", saldo=""):
        konto = cls.Wyszukaj_konto_peselem(pesel)
        if (konto != None):
            if (imie != ""):
                konto.imie = imie
            if (nazwisko != ""):
                konto.nazwisko = nazwisko
            if (saldo != ""):
                konto.saldo = saldo