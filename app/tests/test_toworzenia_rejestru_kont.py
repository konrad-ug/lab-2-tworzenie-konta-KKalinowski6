import unittest

from ..Konto import Konto, Konto_Firmowe
from app.RejestrKont import RejestrKont

class TestRejestru(unittest.TestCase):

    def setUp(self):
        self.konto1 = Konto("Dariusz", "Kot", "55071284252")
        self.konto2 = Konto("Dariusz", "Kot", "55071284253")
        self.konto3 = Konto("Dariusz", "Kot", "55071284254")

    @classmethod
    def setUpClass(cls):
        konto = Konto("Dariusz", "Kot", "55071284261")
        RejestrKont.Dodaj_konto(konto)
    
    def test_1_dodawanie_konta_do_rejestru(self):
        RejestrKont.Dodaj_konto(self.konto1)
        self.assertEqual(RejestrKont().Ile_kont(), 2, "Nie dodano konta do rejestru")

    def test_2_dodawania_konta_do_rejestru(self):
        RejestrKont.Dodaj_konto(self.konto2)
        RejestrKont.Dodaj_konto(self.konto3)
        self.assertEqual(RejestrKont().Ile_kont(), 4, "Nie dodano kont do rejestru")

    def test_3_wyszukaj_konto(self):
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284252").pesel, self.konto1.pesel, "Nie znaleziono konta w rejestrze")
    
    def test_3_wyszukaj_nieistniejace_konto(self):
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284263"), None, "Nie znaleziono konta w rejestrze")

    def test_3_zmien_wartosci_konta(self):
        RejestrKont().Zmien_wartosci_konta({"old_pesel": "55071284261","imie": "Magda","saldo": 100, "nazwisko": "Mal", "pesel":"55071284262"})
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284262").imie, "Magda", "Niezmieniono danych")
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284262").saldo, 100, "Niezmieniono danych")
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284262").nazwisko, "Mal", "Niezmieniono danych")
    
    def test_4_usun_konto_z_rejestru(self):
        RejestrKont().Usun_konto("55071284262")
        self.assertEqual(RejestrKont().Wyszukaj_konto_peselem("55071284262"), None, "Nie usunieto konta")

    @classmethod
    def tearDownClass(cls):
        RejestrKont.list = []

