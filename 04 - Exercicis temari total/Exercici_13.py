# Donada una frase acabada en punt, comptar el nombre d’aparicions del grup ‘la’.

frase = input("Escriu grups de paraules per fer una frase (punt acaba el programa): ")
la = 0

while frase != ".":
    if frase == "la" or frase == "La" or frase == "LA" or frase == "lA":
        la += 1
    frase = input("Escriu grups de paraules per fer una frase (punt acaba el programa): ")

print(f"En la frase hi han {la} paraules 'la'.")
