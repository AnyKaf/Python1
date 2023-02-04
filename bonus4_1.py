def format_cisla(cislo):
    cislo = cislo.replace(" ", "")
    if len(cislo) == 9:
        print("True")
    elif len(cislo) == 13:
        predvolba = "+420"
        if cislo[0:4] == predvolba:
            print("True")
        else:
            print("False")
            quit()
    else:
        print("False")
        quit()

def cena_zpravy(zprava):
    cena = ((len(zprava) // 180) + 1) * 3
    return cena


cislo_zadano = input("Zadejte telefonní číslo: ")
format_cisla(cislo_zadano)

zprava_zadano = input("Zadejte text vaší SMS: ")
cena_final = cena_zpravy(zprava_zadano)
print(f"Cena vaší SMS je {cena_final} Kč")