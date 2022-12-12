import fajlbeolvasas
fajlbeolvasas.beolvas("teszt.txt")
print(f"\nStatisztikák:\n{'='*38}")
fajlbeolvasas.statisztikak()
print(f"\nÚj adat felvitele:\n{'='*20}")
fajlbeolvasas.uj_adatsor_hozzaadasa()
