#Escriure un algorisme que determini si un nombre enter positiu és primer o no.

divisor = 2
nombre = int(input("Escriu un número per saber si és nombre primer: "))
residu = nombre % divisor

while divisor != nombre and residu != 0:
    divisor += 1
    residu = nombre % divisor
    
if divisor == nombre:
    print(f"És nombre primer")
else:
    print(f"No és nombre primer")