import unittest
from unittest.mock import patch

from ..Konto import Konto
from ..Konto_Firmowe import Konto_Firmowe

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "Firma"
    nip = "7772696293"
    nip_pranie = "1111111111"
    krotki_nip = "222"
    dlugi_nip = "1111111111111111111"

    @patch('app.Konto_Firmowe.requests.get', return_value={"status_code":200})
    def test_tworzenie_konta_firmowego(self,mock):
        firma = Konto_Firmowe(self.nazwa_firmy, self.nip)
            
        self.assertEqual(firma.nazwa_firmy, self.nazwa_firmy, "Nazwa firmy nie zostala zapisana")
        self.assertEqual(firma.nip, self.nip, "NIP firmy nie zostala zapisana")
        self.assertEqual(firma.historia, [], "Historia firmy nie zostala utworzona!")

    def test_tworzenie_konta_firmowego_dlugi_nip(self):
        firma_z_dlugim_nipem = Konto_Firmowe(self.nazwa_firmy, self.dlugi_nip)

        self.assertEqual(firma_z_dlugim_nipem.nip, "Niepoprawny NIP!", "Zbyt dlugi NIP firmy nie zostala zapisana")

    def test_tworzenie_konta_firmowego_krotki_nip(self):
        firma_z_krotkim_nipem = Konto_Firmowe(self.nazwa_firmy, self.krotki_nip)

        self.assertEqual(firma_z_krotkim_nipem.nip, "Niepoprawny NIP!", "Zbyt krotki NIP firmy nie zostala zapisana")

    @patch('app.Konto_Firmowe.requests.get', return_value={"status_code":404})
    def test_tworzenie_konta_firmowego_nieistnieje(self, mock):
        firma = Konto_Firmowe(self.nazwa_firmy, self.nip)

        self.assertEqual(firma, False, "Nie wykryto niewlasciwego nipu")