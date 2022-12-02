import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body={
        "imie":"nick",
        "nazwisko":"cave",
        "pesel":"89092909825"
    }

    url = "http://localhost:5000/"

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url+"konta/stworz_konto", json = self.body)
        self.assertEqual(create_resp.status_code, 201)
    
    def test_2_get_po_peselu(self):
        get_resp = requests.get(self.url+f"konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        res_body = get_resp.json()
        self.assertEqual(res_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(res_body["imie"], self.body["imie"])
        self.assertEqual(res_body["saldo"], 0)

    def test_3_get_ile_kont(self):
        get_resp = requests.get(self.url+f"konta/ile_kont")
        self.assertEqual(get_resp.status_code, 200)
        res_body = get_resp.json()
        self.assertEqual(res_body, "Ilosc kont w rejestrze 1")