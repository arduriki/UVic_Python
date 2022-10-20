# Donada una sèrie d’enters acabada en 0, calcular la seva mitjana aritmètica.

count = 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Escriu un número enter (0 per aturar): "))
    
    if numero != 0: #així no suma el zero al final del exercici.
        suma += numero # += vol dir que s'ha de sumar el valor anterior.
        count += 1


if suma == 0:
    print("No has escrit cap número.")
else:
    mitjana = suma / count
    print(f"La mitjana aritmètica dels números introduïts és de: {mitjana}")