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
    def Zmien_wartosci_konta(cls, nowe_wartosci):
        if ("old_pesel" in nowe_wartosci):
            pesel = nowe_wartosci['old_pesel']
            konto = cls.Wyszukaj_konto_peselem(pesel)
            if (konto != None):
                if ("imie" in nowe_wartosci):
                    konto.imie = nowe_wartosci['imie']
                if ("nazwisko" in nowe_wartosci):
                    konto.nazwisko = nowe_wartosci['nazwisko']
                if ("saldo" in nowe_wartosci):
                    konto.saldo = nowe_wartosci['saldo']
                if ("pesel" in nowe_wartosci):
                    konto.pesel = nowe_wartosci['pesel']
    
    @classmethod
    def Usun_konto(cls, pesel):
        konto = cls.Wyszukaj_konto_peselem(pesel)
        if (konto != None):
            cls.list.remove(konto)