#Refer l'exercici 1.1 afegint la nova tarifa d'hora punta: "P" a 25 cèntims/pas.

d = 0.15 #diurna
p = 0.25 #punta
n = 0.1 #nocturna

minuts = float(input("Benvingut/da a la calculadora de trucades! \n Escriu els minuts de la trucada: "))
franja = str(input("Escriu la franja horaria. Sent d diürn, p punta i n nocturn: "))

if franja == "n":
    calcul = (minuts) * (n)
    print(f"La trucada té un import de: {calcul}")
elif franja == "p":
    calcul = (minuts) * (p)
    print(f"La trucada té un import de: {calcul}")
else:
    calcul = (minuts) * (d)
    print(f"La trucada té un import de: {calcul}")