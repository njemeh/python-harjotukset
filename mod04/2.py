while True:
    tuumat = float(input("syötä tuumamäärä (negatiivinen luku lopettaa): "))
    if tuumat < 0:
        print("negatiivinen luku lopettaa ohjelman")
        break
    cm = tuumat * 2.54
    print(f"{tuumat} tuumaa on {cm} senttimetrit")