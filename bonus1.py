jmeno_a_prijmeni = input("Zadejte své celé jméno: ")

jmeno = str(jmeno_a_prijmeni.split() [0])
prijmeni = str(jmeno_a_prijmeni.split() [1])

print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())
print(jmeno[0].upper()+". " + prijmeni[0].upper()+ ".")

if len(jmeno) < 5:
    print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())
else: 
    print(jmeno[0].upper()+". "+ prijmeni[0].upper() + prijmeni[1:].lower())

velke = int(input("Kolikáté písmeno křestního jména chcete velké? "))
print(jmeno[:velke].lower() + jmeno[velke].upper() + jmeno[velke+1:].lower())


