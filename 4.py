import random

tietokoneen_luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1-10: "))
        if arvaus < tietokoneen_luku:
            print("Liian pieni arvaus.")
        elif arvaus > tietokoneen_luku:
            print("Liian suuri arvaus")
        else:
            print("oikein.")
            break
    except ValueError:
        print("Anna kokonaisluku.")