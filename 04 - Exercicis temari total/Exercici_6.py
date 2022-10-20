# Realitzar un algorisme que calculi els divisors d’un nombre donat.

divisor = 1
nombre = int(input("Escriu un número per saber el seus divisors: "))
residu = nombre % divisor

while divisor != nombre:
    if residu == 0:
        print (f"{divisor} és el seu divisor")
    divisor += 1
    residu = nombre % divisor
print(f"{nombre} és el seu divisor")
    