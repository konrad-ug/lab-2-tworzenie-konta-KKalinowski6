import unittest
from parameterized import parameterized

from ..Konto import Konto, Konto_Firmowe

class TestZaciaganiaKredytow(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "55071284261"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)
    
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

