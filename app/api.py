from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto
import json 

app = Flask(__name__)
@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    status=RejestrKont().Dodaj_konto(konto)
    if (status):
        return jsonify("Konto stworzone"), 201
    else:
        return jsonify("Konto juz istnieje"), 400

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return f"Ilosc kont w rejestrze {RejestrKont().Ile_kont()}", 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont().Wyszukaj_konto_peselem(pesel)
    if (konto != None):
        return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200

@app.route("/konta/zmien_dane", methods=['PUT'])
def zmien_wartosci_konta():
    dane = request.get_json()
    print(f"Request o zmiane danych konta: {dane}")
    RejestrKont().Zmien_wartosci_konta(dane)
    return jsonify("Dane zmienione"), 200

@app.route("/konta/usun_konto", methods=['DELETE'])
def usun_konto():
    dane = request.get_json()
    print(f"Request o usuniecie konta z peselem: {dane['pesel']}")
    RejestrKont().Usun_konto(dane['pesel'])
    return jsonify("Konto usuniete"), 200