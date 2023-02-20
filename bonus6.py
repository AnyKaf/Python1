import re

#prihlasovaci jmeno:
while True: 
    prihlasovaci_jmeno = input("Zadejte přihlašovací jméno: ")
    regulerni_vyraz_jmeno = re.compile(r"[a-zA-Z]{6,10}")

    if regulerni_vyraz_jmeno.fullmatch(prihlasovaci_jmeno):
        print("Přihlašovací jméno bylo zadáno správně")
        break
    else:
        print("Přihlašovací jméno nemá správný formát, zkus to znova!")

#heslo:
while True:
    heslo = input("Zadejte heslo: ")
    if len(heslo)<12 or len(heslo)>30:
        print("Heslo nesplňuje požadovanou délku, zkus to znova!")

    else:
        regulerni_vyraz_heslo = re.compile(r"\w*[_.+=-]*\w*")
        if regulerni_vyraz_heslo.fullmatch(heslo):
            print("Heslo bylo zadáno správně:)")
            break
        else:
            print("Heslo obsahuje nepovolené znaky, zkus to znova!")

#email
while True:
    email = input("Zadejte e-mailovou adresu: ")
    regulerni_vyraz_email = re.compile(r"(\w+[\.\+\-])?\w+@\w+((\.\w+)+)")
    if regulerni_vyraz_email.fullmatch(email):
        print("E-mail byl zadán správně!")
        break
    else:
        print("E-mail nemá správný formát, zkus to znova!")



