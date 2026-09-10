#Kysytään kunhan pituus senttimetreinä:))
pituus=float(input("Anna kunhan pituus senttimetreinä: "))

#Tarkistetaan onko kuha alamittainen
if pituus < 37:
    puutuuu = 37 - pituus
    print("Kuha on alamittainen.")
    print(f"laske kuha takaisin järveen. Alimmasta sallitusta pyyntimitasta puutuuu: {puutuuu:.1f}  cm")
else:
    print("Kuha on sallittu pyyntimitan pituinen!")
