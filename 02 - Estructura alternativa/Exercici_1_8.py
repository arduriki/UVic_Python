#Fer un programa que, donat un enter, miri si està entre 2 i 8 (ambdós inclosos) i si no, si és major que
#11 o bé menor que -2. Treure els corresponents missatges.

number = int(input("Escriu un número: "))

if number >= 2 and number <= 8:
    print(f"{number} esta entre 2 i 8")
elif number > 11:
    print(f"{number} és més gran que 11")
elif number < (-2):
    print(f"{number} és més petit que -2")
else:
    print("Ho sento, el número no entra dintre dels paràmetres")