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