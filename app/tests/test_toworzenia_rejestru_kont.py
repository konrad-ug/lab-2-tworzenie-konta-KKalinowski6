import unittest

from ..Konto import Konto, Konto_Firmowe
from app.RejestrKont import RejestrKont

class TestRejestru(unittest.TestCase):

    def setUp(self):
        self.konto = Konto("Dariusz", "Kot", "55071284261")

    @classmethod
    def SetUpClass(cls):
        konto = Konto("Dariusz", "Kot", "55071284261")
        RejestrKont.Dodaj_konto(konto)
    
    def test_1_dodawanie_konta_do_rejestru(self):
        RejestrKont.Dodaj_konto(self.konto)
        self.assertEqual(RejestrKont().Ile_kont(), 1, "Nie dodano konta do rejestru")

    def test_2_dodawania_konta_do_rejestru(self):
        RejestrKont.Dodaj_konto(self.konto)
        RejestrKont.Dodaj_konto(self.konto)
        self.assertEqual(RejestrKont().Ile_kont(), 3, "Nie dodano kont do rejestru")

    def test_wyszukaj_konto(self):
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284263").pesel, self.konto.pesel, "Nie znaleziono konta w rejestrze")
    
    def test_wyszukaj_konto(self):
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284263"), None, "Nie znaleziono konta w rejestrze")

    @classmethod
    def tearDownClass(cls):
        RejestrKont.list = []

