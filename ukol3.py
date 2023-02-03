import json
with open("body.json") as soubor:
    vysledky = json.load(soubor)

novy = {}
for x, y in vysledky.items():
    if y > 60:
        novy[x] = "pass"
    else:
        novy[x] = "fail"
    

with open ("prospech.json", mode = "w", encoding = "utf-8") as fp:
    json.dump(novy, fp, ensure_ascii=False)