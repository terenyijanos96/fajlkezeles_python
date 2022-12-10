def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='utf-8')
    sorok = fajlom.readlines()
    fajl_feldolgozas(sorok)
    fajlom.close()


nevek = []
nemek = []
korok = []


def fajl_feldolgozas(sorok):
    """"itt dolgozom fel az adott listát"""
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip()
        nev, nem, kor = sor.split(", ")
        nevek.append(nev)
        nemek.append(nem)
        korok.append(kor)
        i += 1

    print(nevek, nemek, korok, sep="\n")
