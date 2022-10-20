#Donada una sèrie d’enters acabada en 0, fer un algorisme que determini si la seqüència només està formada per valors positius.

numeros = int(input("Escriu un numero enter (0 acaba el programa): "))
positiu = 0
negatiu = 0

while numeros != 0:
    if numeros > 0:
        positiu += 1
    else:
        negatiu += 1
    numeros = int(input("Escriu un numero enter (0 acaba el programa): "))

if positiu >= 1 and negatiu == 0:
    print("La seqüència és de valors positius.")
elif positiu == 0 and negatiu == 0:
    print("No has introduït cap número.")
else:
    print("La seqüència no és de valors positius.")