import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body={
        "imie":"nick",
        "nazwisko":"cave",
        "pesel":"89092909825"
    }
    body2={
        "old_pesel":"89092909825",
        "pesel":"89092909826",
        "nazwisko":"kot",
        "saldo": 200
    }

    url = "http://localhost:5000/"

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url+"konta/stworz_konto", json = self.body)
        self.assertEqual(create_resp.status_code, 201)
    
    def test_2_tworzenie_kont_istniejacy_pesel(self):
        create_resp = requests.post(self.url+"konta/stworz_konto", json = self.body)
        self.assertEqual(create_resp.status_code, 400)
    
    def test_3_get_po_peselu(self):
        get_resp = requests.get(self.url+f"konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        res_body = get_resp.json()
        self.assertEqual(res_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(res_body["imie"], self.body["imie"])
        self.assertEqual(res_body["saldo"], 0)

    def test_4_put_zmiana_danych(self):
        put_resp = requests.put(self.url+"/konta/zmien_dane", json= self.body2)
        self.assertEqual(put_resp.status_code, 200)

    def test_5_delete_konto(self):
        delete_resp = requests.delete(self.url+"/konta/usun_konto", json= {"pesel": "89092909826"})
        self.assertEqual(delete_resp.status_code, 200)