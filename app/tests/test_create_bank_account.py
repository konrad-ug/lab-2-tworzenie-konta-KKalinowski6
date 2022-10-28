import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        poprawny_pesel = "55071284261"
        niepoprawny_pesel = "666"
        pesel_upowazniony_do_promocji = "65071284261"
        kod_rabatowy = "PROM_XYZ"
        pesel_po_2000 = "01234567898"

        pierwsze_konto = Konto(imie, nazwisko, poprawny_pesel)
        konto_z_kodem = Konto(imie, nazwisko, pesel_upowazniony_do_promocji, kod_rabatowy)
        konto_ze_zlym_peselem = Konto(imie, nazwisko, niepoprawny_pesel)
        konto_ze_zlym_kodem = Konto(imie, nazwisko, poprawny_pesel, "ABC")
        konto_seniora = Konto(imie, nazwisko, poprawny_pesel, kod_rabatowy)
        konto_po_2000 = Konto(imie, nazwisko, pesel_po_2000, kod_rabatowy)

        #feature 1
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        #feature 2
        self.assertEqual(pierwsze_konto.pesel, poprawny_pesel, "Pesel nie został zapisany!")

        #feature 3
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")
        self.assertEqual(konto_ze_zlym_peselem.error, "Error", "Poprawny pesel nie zostal przyjety")

        #feature 4
        self.assertEqual(konto_z_kodem.kod_rabatowy, kod_rabatowy or None, "Niepoprawny kod rabatowy!")
        self.assertNotEqual(konto_ze_zlym_kodem.kod_rabatowy, kod_rabatowy or None, "Przyjeto niepoprawny kod rabatowy!")

        self.assertEqual(konto_z_kodem.saldo, 50, "Nienaliczono promocji!")
        self.assertEqual(konto_ze_zlym_kodem.saldo, 0, "Naliczono promocje ze zlym kodem!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Naliczono promocje bez kodu!")

        #feature 5
        self.assertEqual(konto_z_kodem.saldo, 50, "Nienaliczono promocji!")
        self.assertEqual(konto_seniora.saldo, 0, "Naliczono promocje seniorowi!")
        self.assertEqual(konto_po_2000.saldo, 50, "Nienlaiczono promocji po 2000!")

    #tutaj proszę dodawać nowe testy
