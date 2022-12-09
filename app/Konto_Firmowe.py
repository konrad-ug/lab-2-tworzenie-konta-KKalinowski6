from .Konto import Konto

class Konto_Firmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.Sprawdzanie_NIP(nip)
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.historia = []

    def Sprawdzanie_NIP(self, nip):
        if (len(nip) == 10):
            self.nip =  nip
        else:
            self.nip =  "Niepoprawny NIP!" 

    def Nalicznie_oplaty_za_przelew_ekspresowy(self):
        return 5

    def Sprawdzanie_warunkow_kredytu(self, wartosc):
        if(self.saldo >= 2*wartosc and self.Sprawdzanie_przelewu_ZUS()):
            return True
        return False
    
    def Sprawdzanie_przelewu_ZUS(self):
        return True if (-1775 in self.historia) else False