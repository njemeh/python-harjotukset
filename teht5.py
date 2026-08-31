leiviskat =float(input("Anna leiviskät./n"))
naulat =float(input("Anna naulat./n"))
luodit =float(input("Anna luodit./n"))

#muunnetaan kaikki nauloiksi
#1 leiviskä = 20 naulaa, 1 naula= 32 luotia
kaikki_luodit = (leiviskat*20*32) + (naulat*32) + luodit

#muunnetaan grammoiksi (1 luoti = 13.3 g)
kokonaisgrammat = kaikki_luodit * 13.3
#jaetaan kiloihin ja grammoihin"
kilogrammat = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
