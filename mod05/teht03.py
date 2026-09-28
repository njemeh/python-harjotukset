luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

# Alkuluvut ovat suurempia kuin 1
if luku <= 1:
    on_alkuluku = False
else:
    # Testataan jaollisuutta luvuilla välillä 2 ... luku-1
    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break  # Löytyi tasan menevä jakaja, joten ei ole alkuluku

# Tulostetaan tulos
if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")