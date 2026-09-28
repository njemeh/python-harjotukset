import random

# Kysytään arpakuutioiden lukumäärä
noppien_maara = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

# Heitetään noppia for-silmukassa
for _ in range(noppien_maara):
    heitto = random.randint(1, 6)
    summa += heitto

# Tulostetaan silmälukujen summa
print(f"Silmälukujen summa on: {summa}")