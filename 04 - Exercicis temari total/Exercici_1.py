#Donada una frase (lletra per lletra) acabada en punt, comptar el nombre d’aparicions de la lletra ‘a’.

frase = input("Escriu una frase lletra per lletra: ")
count_a = int(0)

while frase != ".":
    if frase == "a" or frase == "A":
        count_a = count_a + 1
    frase = input("Continua escrivint: ")
print(f"S'han comptat {count_a} lletres a en la frase.")
