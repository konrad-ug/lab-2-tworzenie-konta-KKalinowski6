import unittest
from parameterized import parameterized
from unittest.mock import patch

from ..Konto import Konto
from ..Konto_Firmowe import Konto_Firmowe

class TestZaciaganiaKredytow(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "55071284261"
    nazwa_firmy = "Firma"
    nip = "1234567890"

    @patch('app.Konto_Firmowe.Konto_Firmowe.sprawdz_nip_gov', return_value=True)
    def setUp(self,mock):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)
    
    @parameterized.expand([
        ([1000, -100, 100, 100, 100], 200, True, 200),
        ([1000, -800, 100, 100, 100], 600, False, 0),
        ([1000, -100, -100, -100, 100], 300, False, 0),
        ([100, 100, 100], 100, False, 0),
        ([1000, -100, 0, 0, 100], 150, True, 150),
        ([], 200, False, 0)
    ])
    def test_przyznawanie_kredytu_dla_konta(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        kredyt_wynik = self.konto.Zaciagnij_kredyt(kwota)
        self.assertEqual(kredyt_wynik, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

    @parameterized.expand([
        ([-225,1000,-1775,2000,4000], 5000, 1000, True, 6000),
        ([-225,1000,-1775,2000,4000], 5000, 3000, False, 5000),
        ([1000,-2000,2000,4000], 5000, 1000, False, 5000),
        ([225,1000,1775,-2000,4000], 5000, 3000, False, 5000),
        ([], 0, 1000, False, 0),
    ])
    def test_przyznawanie_kredytu_dla_konta_firmowego(self, historia, saldo, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto_firmowe.historia = historia
        self.konto_firmowe.saldo = saldo
        kredyt_wynik = self.konto_firmowe.Zaciagnij_kredyt(kwota)
        self.assertEqual(kredyt_wynik, oczekiwany_wynik)
        self.assertEqual(self.konto_firmowe.saldo, oczekiwane_saldo)
