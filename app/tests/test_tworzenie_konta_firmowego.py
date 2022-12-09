import unittest

from ..Konto import Konto
from ..Konto_Firmowe import Konto_Firmowe

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "Firma"
    nip = "1234567890"
    krotki_nip = "222"
    dlugi_nip = "1111111111111111111"

    def test_tworzenie_konta_firmowego(self):
        firma = Konto_Firmowe(self.nazwa_firmy, self.nip)
        firma_z_krotkim_nipem = Konto_Firmowe(self.nazwa_firmy, self.krotki_nip)
        firma_z_dlugim_nipem = Konto_Firmowe(self.nazwa_firmy, self.dlugi_nip)

        self.assertEqual(firma.nazwa_firmy, self.nazwa_firmy, "Nazwa firmy nie zostala zapisana")
        self.assertEqual(firma.nip, self.nip, "NIP firmy nie zostala zapisana")
        self.assertEqual(firma_z_krotkim_nipem.nip, "Niepoprawny NIP!", "Zbyt krotki NIP firmy nie zostala zapisana")
        self.assertEqual(firma_z_dlugim_nipem.nip, "Niepoprawny NIP!", "Zbyt dlugi NIP firmy nie zostala zapisana")
    
        self.assertEqual(firma.historia, [], "Historia firmy nie zostala utworzona!")

    def test_przelewy_firmowe(self):
        firma = Konto_Firmowe(self.nazwa_firmy, self.nip)

        firma.Przelew_przychodzacy(50)
        self.assertEqual(firma.saldo, 50, "Nie przychodzacy")