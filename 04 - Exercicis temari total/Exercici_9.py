#Escriure un algorisme que faci la còpia d’un text acabat en punt suprimint tots els espais en blanc.

frase = input("Escriu una frase lletra a lletra amb espais (punt acaba el programa): ")

while frase != ".":
    if frase != " ":
        print(frase)
    frase = input("Escriu la següent lletra o espai (punt acaba el programa): ")