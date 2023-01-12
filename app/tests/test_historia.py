import unittest
from unittest.mock import patch, MagicMock
from datetime import date

from ..Konto import Konto
from ..SMTPConnection import SMTPConnection
from ..Konto_Firmowe import Konto_Firmowe

class TestHistoria(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "55071284261"
    nazwa_firmy="Firma"
    nip="1234567890"

    def test_wysylanie_maila_z_historia(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [300,400,-200]
        smpt_connector = SMTPConnection()
        smpt_connector.wyslij = MagicMock(return_value = True)
        self.assertTrue(konto.Wyslij_historie_na_maila("email@email.com", smpt_connector))
        smpt_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today()}", f"Twoja historia konta to: {konto.historia}", "email@email.com")
    
    def test_wysylanie_maila_z_historia_niepowodzenie(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [300,400,-200]
        smpt_connector = SMTPConnection()
        smpt_connector.wyslij = MagicMock(return_value = False)
        self.assertFalse(konto.Wyslij_historie_na_maila("email@email.com", smpt_connector))

    @patch('app.Konto_Firmowe.Konto_Firmowe.sprawdz_nip_gov', return_value=True)
    def test_wysylanie_maila_z_historia_dla_konta_firmowego(self, mock):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.historia = [300,400,-200]
        smpt_connector = SMTPConnection()
        smpt_connector.wyslij = MagicMock(return_value = True)
        self.assertTrue(konto_firmowe.Wyslij_historie_na_maila("email@email.com", smpt_connector))
        smpt_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today()}", f"Historia konta Twojej firmy to: {konto_firmowe.historia}", "email@email.com")

    @patch('app.Konto_Firmowe.Konto_Firmowe.sprawdz_nip_gov', return_value=True)
    def test_wysylanie_maila_z_historia_dla_konta_firmowego_niepowodzenie(self, mock):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.historia = [300,400,-200]
        smpt_connector = SMTPConnection()
        smpt_connector.wyslij = MagicMock(return_value = False)
        self.assertFalse(konto_firmowe.Wyslij_historie_na_maila("email@email.com", smpt_connector))