str_a = input("Zahl 1: ")
try:
    int_a = int(str_a)
except:
    print("Ihr Input ist keine Zahl")
    exit()

str_b = input("Zahl 2: ")
try:
    int_b = int(str_b)
except:
    print("Ihr Input ist keine Zahl")
    exit()
    
if int_b == 0:
    print("man kann nicht durch 0 dividieren, Dummkopf")
    
else:
    int_summe = int_a + int_b
    int_diff = int_a - int_b
    int_div = int_a / int_b
    int_prod = int_a + int_b
    print("SUMME: Zahl 1 + Zahl 2 = " + int_summe + "\n")
    print("DIFFERENZ: Zahl 1 - Zahl 2 = " + int_diff + "\n")
    print("DIVISION: Zahl 1 / Zahl 2 = " + int_div + "\n")
    print("PRODUKT: Zahl 1 * Zahl 2 = " + int_prod + "\n")