import random

nevek = []
nemek = []
korok = []


def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='utf-8')
    sorok = fajlom.readlines()
    fajl_feldolgozas(sorok)
    fajlom.close()


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


def rogzitett_adatok_szama():
    c = 0

    i = 1
    while i < len(nevek):
        c += 1
        i += 1

    i = 1
    while i < len(nemek):
        c += 1
        i += 1

    i = 1
    while i < len(korok):
        c += 1
        i += 1

    return c


def atlagos_eletkor():
    osszeg = 0
    i = 1
    while i < len(korok):
        osszeg += int(korok[i])
        i += 1

    return osszeg / (len(korok) - 1)


def nok_szama():
    c = 0
    i = 1
    while i < len(nemek):
        if nemek[i] == "nő":
            c += 1
        i += 1

    return c


def legfiatalabb_no_eletkora():
    i = 1
    minimum = 200
    while i < len(nemek):
        if nemek[i] == "nő":
            kor = int(korok[i])
            if kor < minimum:
                minimum = kor
        i += 1

    return minimum


def statisztikak():
    print("A fájlban rögzített adatok száma:", rogzitett_adatok_szama())
    print("Emberek átlagéletkora:", atlagos_eletkor())
    print("A listában ennyi nő szerepel:", nok_szama())
    print("A legfiatalabb nő életkora:", legfiatalabb_no_eletkora())


def uj_adatsor_hozzaadasa():
    nev = input("Kérek egy nevet: ").capitalize()
    nem = input("Kérem adja meg a nemet (férfi, vagy nő lehet): ")
    while nem not in ("férfi", "nő"):
        nem = input('HIBA! Rossz értéket adott meg a nemnek! (Helyes értékek: férfi, nő): ')

    kor = str(int(random.random() * 71) + 10)

    f = open("teszt.txt", "a", encoding='utf-8')
    f.write(f"\n{nev}, {nem}, {kor}")
    f.close()
