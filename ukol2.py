sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Zadejte kód součástky: ")

if soucastka in sklad.keys():
    mnozstvi = int(input("Kolik si jich přejete? "))
    mnozstvi_sklad = sklad[soucastka]
    if mnozstvi > mnozstvi_sklad: 
        print (f"Na skladě nemáme pouze {sklad[soucastka]}ks")
        sklad.pop(soucastka)
        print(f"Součástka bude prodána v maximálním množství {mnozstvi_sklad} ks. ")
        print(f"Dále máme na skladě: {sklad}. ")
    else:
        print(f"Vámi zadaná součástka {soucastka} Vám bude doručena v množství {mnozstvi} ks. Děkujeme za nákup!")
        zbytek = mnozstvi_sklad - mnozstvi
        print(f"Na skladě nám zbývá {zbytek} ks")
else: 
    print("Vámi zadanou součástku nemáme na skladě :(")