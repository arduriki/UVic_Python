#Donada una frase acabada en punt, comptar el nombre de caràcters que hi apareixen des del principi.

frase = input("Escriu una frase lletra a lletra: ")
count_caracters = int(0)

while frase != ".":
    count_caracters = count_caracters +1
    frase = input("Escriu una frase lletra a lletra: ")

print(f"La frase té {count_caracters} caracters.")