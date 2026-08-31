import random
#kolmenumeroinen koodi (merkit 0-9)
koodi1_n1 = random.randint(0,9)
koodi1_n2=random.randint(0,9)
koodi1_n3=random.randint(0,9)

#Nelinumeroinen koodi (merkit 1-6)
koodi2_n1=random.randint(1,6)
koodi2_n2=random.randint(1,6)
koodi2_n3=random.randint(1,6)
koodi2_n4=random.randint(1,6)
print(f"Kolmenumeroinen koodi: {koodi1_n1}{koodi1_n2}{koodi1_n3}")
print(f"Nelinumeroinen koodi: {koodi2_n1}{koodi2_n2}{koodi2_n3}{koodi2_n4}")