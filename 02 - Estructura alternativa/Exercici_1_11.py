#Fer un programa que incrementi un nombre binari. Ha de llegir tres nombres, que seran zeros o uns,
#que representen un nombre binari de tres bits. S'incrementarà en u aquest nombre i s'escriurà el
#resultat.

b1 = int(input("Escriu el primer bit en binari: "))
b2 = int(input("Escriu el segon bit en binari: "))
b3 = int(input("Escriu el tercer bit en binari: "))

if b1 >= 1:
    b1 = 0
    b2 = b2 + 1
    if b2 >= 1:
        b2 = 0
        b3 = b3 + 1
        if b3 >= 1:
            b3 = 0
            print(f"Els bits són: {b3} {b2} {b1}.")
        else:
            print(f"Els bits són: {b3} {b2} {b1}.")
    else:
        print(f"Els bits són: {b3} {b2} {b1}.")
else:
    b1 = b1 + 1
    print(f"Els bits són: {b3} {b2} {b1}.")
