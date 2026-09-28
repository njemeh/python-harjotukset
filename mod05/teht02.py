luvut = []

while True:
    syote = input("Syötä luku (tyhjä lopettaa): ")
    if syote == "":
        break
    
    # Muunnetaan syöte luvuksi ja lisätään listaan
    luku = float(syote)
    luvut.append(luku)

# Järjestetään lista suurimmasta pienimpään
luvut.sort(reverse=True)

print("\Viisi suurinta lukua suurimmasta alkaen:")
# Tulostetaan viisi ensimmäistä (tai vähemmän, jos lukuja syötettiin vähän)
for luku in luvut[:5]:
    print(luku)