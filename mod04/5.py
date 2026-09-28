Oikea_tunnus = " Opiskelija"
Oikea_salasana = " Salasisuus"
yritykset = 0

while yritykset < 5:
    tunnus = input(" käyttäjätunnus: ")
    salasana = input(" salasana: ")

    if tunnus == Oikea_tunnus and salasana == Oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        
        print(f"Väärä tunnus tai salasana. ")
        yritykset += 1

    if yritykset == 5:
        print("pääsy evätty")
