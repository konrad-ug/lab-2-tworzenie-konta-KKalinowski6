import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        poprawny_pesel = "55071284261"
        krotki_pesel = "666"
        dlugi_pesel = "1234563546125512"

        pierwsze_konto = Konto(imie, nazwisko, poprawny_pesel)
        konto_z_krotkim_peselem = Konto(imie, nazwisko, krotki_pesel)
        konto_z_dlugim_peselem = Konto(imie, nazwisko, dlugi_pesel)

        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        self.assertEqual(pierwsze_konto.pesel, poprawny_pesel, "Pesel nie został zapisany!")

        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")
        self.assertEqual(konto_z_dlugim_peselem.error, "Error", "Niepoprawny pesel zostal przyjety")
        self.assertEqual(konto_z_krotkim_peselem.error, "Error", "Niepoprawny pesel zostal przyjety")
    
    def test_naliczanie_promocji_do_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel_seniora = "55071284261"
        pesel_upowazniony_do_promocji = "65071284261"
        kod_rabatowy = "PROM_XYZ"
        pesel_po_2000 = "01234567898"

        konto_bez_kodu = Konto(imie, nazwisko, pesel_po_2000)
        konto_ze_zlym_kodem = Konto(imie, nazwisko, pesel_upowazniony_do_promocji, "ABC")
        konto_upowaznione_do_promocji = Konto(imie, nazwisko, pesel_upowazniony_do_promocji, kod_rabatowy)    
        konto_seniora = Konto(imie, nazwisko, pesel_seniora, kod_rabatowy)
        konto_po_2000 = Konto(imie, nazwisko, pesel_po_2000, kod_rabatowy)
        
        self.assertEqual(konto_bez_kodu.kod_rabatowy, None, "Zapisano kod rabotwy inny niz None!")
        self.assertEqual(konto_upowaznione_do_promocji.kod_rabatowy, kod_rabatowy, "Niezapisano kodu rabatowego!")
        self.assertEqual(konto_ze_zlym_kodem.kod_rabatowy, "ABC", "Niezapisano kodu rabatowego!")

        self.assertEqual(konto_upowaznione_do_promocji.saldo, 50, "Nienaliczono promocji!")
        self.assertEqual(konto_ze_zlym_kodem.saldo, 0, "Naliczono promocje ze zlym kodem!")
        self.assertEqual(konto_bez_kodu.saldo, 0, "Naliczono promocje bez kodu!")

        self.assertEqual(konto_seniora.saldo, 0, "Naliczono promocje seniorowi!")
        self.assertEqual(konto_po_2000.saldo, 50, "Nienlaiczono promocji po 2000!")

    #tutaj proszę dodawać nowe testy
