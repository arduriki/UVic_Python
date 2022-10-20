#Donada una frase acabada en punt, comptar el nombre de vocals que hi apareixen

frase = input("Escriu una frase lletra per lletra: ")
compte_vocals = 0

while frase != ".":
    if frase == "a" or frase == "e" or frase == "i" or frase == "o" or frase == "u":
        compte_vocals = compte_vocals + 1
    frase = input("Continua escrivint: ")

print(f"Hi ha {compte_vocals} vocals.")