import unittest

from ..Konto import Konto, Konto_Firmowe

class TestZaciaganiaKredytow(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "55071284261"
    
    def test_akceptowanie_kredytu(self):
        konto_z_trzech_wplat_i_dobra_suma = Konto(self.imie,self.nazwisko,self.pesel)
        konto_z_trzech_wplat_i_dobra_suma.historia = [1000, -100, 100, 100, 100]
        kredyt_wynik = konto_z_trzech_wplat_i_dobra_suma.Zaciagnij_kredyt(200)
        self.assertEqual(kredyt_wynik, True, "Warunki spelnione, niezaakaceptowano kredytu")
        self.assertEqual(konto_z_trzech_wplat_i_dobra_suma.saldo, 200, "Warunki splenione, nie naliczono do salda")

    def test_odrzucanie_kredytu(self):
        konto_z_trzech_wplat_i_zla_suma = Konto(self.imie,self.nazwisko,self.pesel)
        konto_bez_trzech_wplat_i_dobra_suma = Konto(self.imie,self.nazwisko,self.pesel)
        konto_bez_trzech_wplat_i_zla_suma = Konto(self.imie,self.nazwisko,self.pesel)

        konto_z_trzech_wplat_i_zla_suma.historia = [1000, -800, 100, 100, 100]
        kredyt_wynik = konto_z_trzech_wplat_i_zla_suma.Zaciagnij_kredyt(600)
        self.assertEqual(kredyt_wynik, False, "Zla suma 5, zaakaceptowano kredyt")
        self.assertEqual(konto_z_trzech_wplat_i_zla_suma.saldo, 0, "Zlas suma 5 przelewow, zmianono saldo")

        konto_bez_trzech_wplat_i_dobra_suma.historia = [1000, -100, -100, -100, 100]
        kredyt_wynik = konto_bez_trzech_wplat_i_dobra_suma.Zaciagnij_kredyt(200)
        self.assertEqual(kredyt_wynik, False, "Zle ostatnie 3 wplaty, zaakaceptowano kredyt")
        self.assertEqual(konto_bez_trzech_wplat_i_dobra_suma.saldo, 0, "Zle ostatnie 3 wplaty, zmieniono saldo")

        konto_bez_trzech_wplat_i_zla_suma.historia = [1000, -800, -100, 100, 100]
        kredyt_wynik = konto_bez_trzech_wplat_i_zla_suma.Zaciagnij_kredyt(200)
        self.assertEqual(kredyt_wynik, False, "Oba warunki nie spelnione, zaakaceptowano kredyt")
        self.assertEqual(konto_bez_trzech_wplat_i_zla_suma.saldo, 0, "Oba warunki nie spelnione, zmieniono saldo")
    
    def test_przyznawanie_kredytu_krotka_historia(self):
        konto_za_krotka_historia = Konto(self.imie,self.nazwisko,self.pesel)
        konto_za_krotka_historia.historia = [100, 100, 100]
        kredyt_wynik = konto_za_krotka_historia.Zaciagnij_kredyt(200)
        self.assertEqual(kredyt_wynik, False, "Niewystarczajaca wielkosc historii, zaakaceptowano kredyt")
        self.assertEqual(konto_za_krotka_historia.saldo, 0, "Niewystarczajaca wielkosc historii, zmieniono saldo")

