import random

i = 0
lotto =[]


int_tipps = int(input("Bitte geben Sie ein, wie viele Tipps sie abgeben möchten: "))

if int_tipps <=5:
    while i <int_tipps:
        x = random.randint(1,45)
        if x in lotto:
            i = i
        else:
            lotto.append(x)
            i+=1

    print("Ihre Zufällig generierten Tipps lauten: ", lotto)

else:
    print("Die maximale Anzahl der Ziehungen lautet 5!")



