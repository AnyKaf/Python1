class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km) -> None:
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne == True:
            print("Potvrzuji zapůjčení vozidla.")
            self.dostupne = False
        else:
            print("Vozidlo není k dispozici.")

    def get_info(self):
        return f"Vozidlo: {self.typ_vozidla}, SPZ: {self.registracni_znacka}"

#auta
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)


zakazka = input("Jaké si přejete auto? ")

if zakazka == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
elif zakazka == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
else:
    print("Tuto značku bohužel zatím nenabízíme :(")

