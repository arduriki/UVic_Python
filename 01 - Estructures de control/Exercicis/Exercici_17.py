#Donada una seqüència com la de l'exercici 13, comptar quantes vegades repeteix la qualitat obtinguda pel primer producte analitzat.

first = input("Give me a quality product: ")
repeat = 0
quality = " "

while quality != "*":
    if quality == first:
        repeat = repeat + 1
    quality = input("Give me a quality product: ")

print(f"You have {repeat} first quality products repeated")