from datetime import date

class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy = None):
        if (len(pesel) == 11):
            self.imie = imie
            self.nazwisko = nazwisko
            self.pesel = pesel
            self.kod_rabatowy = kod_rabatowy
            self.Naliczanie_promocji()
            self.historia = []
        else:
            self.error = "Error"

    def Naliczanie_promocji(self):
        if (self.kod_rabatowy == "PROM_XYZ" and (int(self.pesel[0:2]) > 60 or int(self.pesel[2]) > 1)):
            self.saldo = 50
        else:
            self.saldo = 0

    def Przelew_przychodzacy(self, wartosc):
        self.saldo += wartosc
        self.historia.append(wartosc)

    def Przelew_wychodzacy(self, wartosc):
        if (self.saldo - wartosc >= 0):
            self.saldo -= wartosc
            self.historia.append(-wartosc)

    def Ekspresowy_przelew_wychodzacy(self, wartosc):
        if(self.saldo - wartosc - self.Nalicznie_oplaty_za_przelew_ekspresowy() >= 0):
            self.saldo -= wartosc + self.Nalicznie_oplaty_za_przelew_ekspresowy()
            self.historia.extend([-wartosc, -self.Nalicznie_oplaty_za_przelew_ekspresowy()])

    def Nalicznie_oplaty_za_przelew_ekspresowy(self):
        return 1

    def Zaciagnij_kredyt(self, wartosc):
        if(self.Sprawdzanie_warunkow_kredytu(wartosc)):
            self.saldo += wartosc
            return True
        else:
            return False

    def Sprawdzanie_warunkow_kredytu(self, wartosc):
        if(len(self.historia) >= 5):
            if(self.Sprawdzanie_5_ostatnich(wartosc) and self.Sprawdzanie_3_ostatnich()):
                return True
        return False

    def Sprawdzanie_5_ostatnich(self, wartosc):
        return True if (sum(self.historia[-5:]) > wartosc) else False

    def Sprawdzanie_3_ostatnich(self):
        return False if(min(self.historia[-3:]) < 0) else True

    def Wyslij_historie_na_maila(self, adresat, smtp_connector):
        temat = f"Wyciąg z dnia {date.today()}"
        tresc = f"{self.Tresc_maila()} {self.historia}"
        
        powodzenie = smtp_connector.wyslij(temat, tresc, adresat)
        if (powodzenie):
            return True
        else:
            return False
    
    def Tresc_maila(self):
        return "Twoja historia konta to:"