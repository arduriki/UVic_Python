#Calcular la suma dels nombres de l'1 al 100. (1+2+3+...+100)

suma_total = int(0)
seguent = int(1)

while seguent <= 100:
    suma_total = int(suma_total) + int(seguent)
    seguent = int(seguent + 1)

print (f"La suma total dels 100 numeros és: {number}")