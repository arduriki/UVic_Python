# Donada una frase acabada en punt, comptar el nombre de caràcters que hi apareixen a partir d’un caràcter donat

frase = input("Escriu una frase lletra a lletra fins que acabi en punt: ")
caracter = "a"
count_caracter = 0
count_frase = 0

while frase != ".":
    count_frase += 1
    if frase == caracter:
        count_caracter += 1
    frase = input("Escriu un altra lletra: ")
        

if count_frase == 0:
    print("No has escrit cap lletra")
else:
    print(f"Hi han {count_caracter} lletres {caracter}")