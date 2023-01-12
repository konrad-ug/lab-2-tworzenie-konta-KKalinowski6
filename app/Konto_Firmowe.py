from .Konto import Konto
import requests
from datetime import date
import os

class Konto_Firmowe(Konto):
    def __new__(cls, nazwa_firmy, nip):
        if cls.Sprawdzanie_poprawnosci_NIP(nip) == "Pranie!":
            return False
        return super().__new__(cls)

    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.historia = []
        self.nip=self.Sprawdzanie_poprawnosci_NIP(nip)

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
            if cls.czy_nip_istnieje(nip):
                return nip
            else:
                return "Pranie!"
        else:
            return "Niepoprawny NIP!"
    
    @classmethod
    def czy_nip_istnieje(cls,nip):
        get_url = os.getenv('BANK_APP_MF_URL', 'https://wl-api.mf.gov.pl/')
        today_date = date.today()
        url = f"{get_url}api/search/nip/{nip}?date={today_date}"
        return cls.sprawdz_nip_gov(url)

    @classmethod
    def sprawdz_nip_gov(cls, url):
        return requests.get(url)["status_code"] == 200

    def Tresc_maila(self):
        return "Historia konta Twojej firmy to:"