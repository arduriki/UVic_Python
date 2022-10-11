#Calcular la suma dels quadrats dels 10 primers nombres.

nombre = 1
calcul = 0

while nombre <= 10: #el tope és 10
    calcul = nombre ** 2 + calcul
    nombre = nombre + 1
    
print(f"La suma dels quadrats dels 10 primers nombres és: {calcul}")