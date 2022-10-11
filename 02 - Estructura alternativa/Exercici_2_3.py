#Escriure les sumes parcials de l'exercici anterior. (1, 1+2, 1+2+3...)

number = int(0)
next = int(1)

while next != 100:
    number = int(number) + int(next)
    next = int(next + 1)
    print(number)

print (f"La suma total dels 100 numeros és: {number}")