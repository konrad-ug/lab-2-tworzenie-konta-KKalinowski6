from .Konto import Konto
import requests
from datetime import date
import os

class Konto_Firmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.historia = []
        if not self.Sprawdzanie_poprawnosci_NIP(nip):
            self.nip="Pranie!"
        else:
            self.nip=nip

    def Nalicznie_oplaty_za_przelew_ekspresowy(self):
        return 5

    def Sprawdzanie_warunkow_kredytu(self, wartosc):
        if(self.saldo >= 2*wartosc and self.Sprawdzanie_przelewu_ZUS()):
            return True
        return False
    
    def Sprawdzanie_przelewu_ZUS(self):
        return True if (-1775 in self.historia) else False

    @classmethod
    def Sprawdzanie_poprawnosci_NIP(cls, nip):
        if (len(nip) == 10):
            get_url = os.getenv("BANK_APP_MF_URL", "https://wl-api.mf.gov.pl/")
            today_date = date.today()
            get_resp = requests.get(f"{get_url}api/search/nip/{nip}?date={today_date}")
            if (get_resp.status_code == 200):
                return True
            else:
                return False
        else:
            return False