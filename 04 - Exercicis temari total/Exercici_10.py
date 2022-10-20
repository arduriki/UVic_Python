#Donada una frase acabada en punt, comptar el nombre de paraules que comencen per ‘a’.

lletra = input("Escriu una frase lletra a lletra amb espais (punt acaba el programa): ")
espai = " "
lletra_a = 0

if lletra == "a" or lletra == "A":
    lletra_a += 1
    lletra = input("Escriu una frase lletra a lletra amb espais (punt acaba el programa): ")

while lletra != ".":
    if lletra == " ":
        lletra = input("Escriu una frase lletra a lletra amb espais (punt acaba el programa): ")
        if lletra == "a" or lletra == "A":
            lletra_a += 1
    lletra = input("Escriu una frase lletra a lletra amb espais (punt acaba el programa): ")

print(f"Hi ha {lletra_a} paraules que comencen per la lletra a.")