euros = int(input("Write how many euros you have: "))

note500 = euros // 500 #divideix la quantitat d'euros per 500
if note500 != 0: #! diferent / si no es compleix, no facis res
    print("You have " + str(note500) + " five hundred euros note/s")
euros = euros % 500 #euros que queden

#else: sino fes això
#while és el mateix que el if, però se'n torna cap a dalt i entra en bucle quan es va complint.
