import unittest

from ..Konto import Konto, Konto_Firmowe

class TestKsiegowaniaOperacji(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "55071284261"

    nazwa_firmy="Firma"
    nip="1234567890"

    def test_ksiegowanie_przelewow_przychodzacych(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)

        konto.Przelew_przychodzacy(50)
        self.assertEqual(konto.saldo, 50, "Przelew nie przyszedl!")

    def test_ksiegowanie_przelewow_przychodzacych_dla_kont_firmowych(self):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)

        konto_firmowe.Przelew_przychodzacy(50)
        self.assertEqual(konto_firmowe.saldo, 50, "Przelew nie przyszedl!")

    def test_ksiegowanie_przelewow_wychodzacych(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500

        konto.Przelew_wychodzacy(500)
        self.assertEqual(konto.saldo, 0, "Przelew nie wyszedl!")

        konto.Przelew_wychodzacy(50)
        self.assertEqual(konto.saldo, 0, "Przelew wyszedl mimo braku srodkow!")

    def test_ksiegowanie_przelewow_wychodzacych_dla_kont_firmowych(self):
        konto_firmowe=Konto_Firmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.saldo = 500

        konto_firmowe.Przelew_wychodzacy(500)
        self.assertEqual(konto_firmowe.saldo, 0, "Przelew nie wyszedl!")

        konto_firmowe.Przelew_wychodzacy(50)
        self.assertEqual(konto_firmowe.saldo, 0, "Przelew wyszedl mimo braku srodkow!")

    def test_seria_przelewow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)

        konto.Przelew_przychodzacy(500)
        konto.Przelew_wychodzacy(300)
        konto.Przelew_wychodzacy(100)
        konto.Przelew_przychodzacy(50)
        konto.Przelew_przychodzacy(50)
        konto.Przelew_wychodzacy(201)
        self.assertEqual(konto.saldo, 200, "Seria nie zostala operowana!")

    def test_seria_przelewow_dla_kont_firmowych(self):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)

        konto_firmowe.Przelew_przychodzacy(500)
        konto_firmowe.Przelew_wychodzacy(300)
        konto_firmowe.Przelew_wychodzacy(100)
        konto_firmowe.Przelew_przychodzacy(50)
        konto_firmowe.Przelew_przychodzacy(50)
        konto_firmowe.Przelew_wychodzacy(201)
        self.assertEqual(konto_firmowe.saldo, 200, "Seria nie zostala operowana!")

    def test_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)

        konto.saldo = 100
        konto.Ekspresowy_przelew_wychodzacy(50)
        self.assertEqual(konto.saldo, 49, "Przelew ekspresowy nie wyszedl!")
        konto.Ekspresowy_przelew_wychodzacy(49)
        self.assertEqual(konto.saldo, 49, "Przelew eksresowy wyszedl mimo braku srodkow!")

    def test_przelew_ekspresowy_dla_kont_firmowych(self):
        konto_firmowe= Konto_Firmowe(self.nazwa_firmy, self.nip)

        konto_firmowe.saldo = 100
        konto_firmowe.Ekspresowy_przelew_wychodzacy(50)
        self.assertEqual(konto_firmowe.saldo, 45, "Przelew ekspresowy konta firmowego nie wyszedl!")
        konto_firmowe.Ekspresowy_przelew_wychodzacy(41)
        self.assertEqual(konto_firmowe.saldo, 45, "Przelew eksresowy konta firmowego wyszedl mimo braku srodkow!")

    def test_kiegowanie_historii_przelewow_przychodzacych(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)

        konto.Przelew_przychodzacy(100)
        self.assertEqual(konto.historia, [100], "Przelew przychodzacy nie znalazł sie w historii!")

    def test_kiegowanie_historii_przelewow_przychodzacych_dla_kont_firmowych(self):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)

        konto_firmowe.Przelew_przychodzacy(100)
        self.assertEqual(konto_firmowe.historia, [100], "Przelew przychodzacy nie znalazł sie w historii!")

    def test_kiegowanie_historii_przelewow_wychodzacych(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)

        konto.saldo = 120
        konto.Przelew_wychodzacy(100)
        self.assertEqual(konto.historia, [-100], "Przelew wychodzacy nie znalazł sie w historii!")
        konto.Przelew_wychodzacy(50)
        self.assertEqual(konto.historia, [-100], "Nie możliwy przelew wychodzacy znalazł sie w historii!")

    def test_kiegowanie_historii_przelewow_wychodzacych_dla_kont_firmowych(self):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)

        konto_firmowe.saldo = 120
        konto_firmowe.Przelew_wychodzacy(100)
        self.assertEqual(konto_firmowe.historia, [-100], "Przelew wychodzacy nie znalazł sie w historii!")
        konto_firmowe.Przelew_wychodzacy(50)
        self.assertEqual(konto_firmowe.historia, [-100], "Nie możliwy przelew wychodzacy znalazł sie w historii!")

    def test_kiegowanie_historii_serii_przelewow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)

        konto.Przelew_przychodzacy(200)
        konto.Przelew_wychodzacy(100)
        konto.Przelew_przychodzacy(30)
        konto.Przelew_wychodzacy(200)
        konto.Przelew_wychodzacy(120)
        self.assertEqual(konto.historia, [200,-100,30,-120], "Seria przelewow nie znalazla sie w historii")

    def test_kiegowanie_historii_serii_przelewow_dla_kont_firmowych(self):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)

        konto_firmowe.Przelew_przychodzacy(200)
        konto_firmowe.Przelew_wychodzacy(100)
        konto_firmowe.Przelew_przychodzacy(30)
        konto_firmowe.Przelew_wychodzacy(200)
        konto_firmowe.Przelew_wychodzacy(120)
        self.assertEqual(konto_firmowe.historia, [200,-100,30,-120], "Seria przelewow nie znalazla sie w historii")

    def test_kiegowanie_historii_przelewow_ekspresowych(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)

        konto.saldo = 70
        konto.Ekspresowy_przelew_wychodzacy(60)
        self.assertEqual(konto.historia, [-60, -1], "Przelew ekspresowy nie znalazl sie w historii")
        konto.Ekspresowy_przelew_wychodzacy(20)
        self.assertEqual(konto.historia, [-60, -1], "Niemozliwy przelew ekspresowy znalazl sie w historii")
    
    def test_kiegowanie_historii_przelewow_ekspresowych_dla_kont_firmowych(self):
        konto_firmowe = Konto_Firmowe(self.nazwa_firmy, self.nip)

        konto_firmowe.saldo = 70
        konto_firmowe.Ekspresowy_przelew_wychodzacy(60)
        self.assertEqual(konto_firmowe.historia, [-60, -5], "Przelew ekspresowy nie znalazl sie w historii")
        konto_firmowe.Ekspresowy_przelew_wychodzacy(20)
        self.assertEqual(konto_firmowe.historia, [-60, -5], "Niemozliwy przelew ekspresowy znalazl sie w historii")