#kysytään sukupuoli ja hemoglobiiniarvo
sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ").lower()
heb = float(input("Anna hemoglobiiniarvo (g/dl): "))
#Tarkistetaan arvo sukupuolen mukaan
if sukupuoli == "nainen":
    if heb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif 117 <= heb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if heb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif 134 <= heb <= 195:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print(" tuntematon sukupuoli. syötä 'nainen' tai 'mies'.")