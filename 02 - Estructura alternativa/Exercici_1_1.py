#Fer un programa que calculi l'import d'una trucada telefònica. Li entrarem el nombre de passes i el tipus de tarifa: "D" per diürna (15 cèntims/pas) o "N" per nocturna (10 cèntims/pas).

d = 0.15
n = 0.1

minuts = float(input("Benvingut/da a la calculadora de trucades! \n Escriu els minuts de la trucada: "))
franja = str(input("Escriu la franja horaria. Sent d diürn i n nocturn: "))

if franja == "n":
    calcul = (minuts) * (n)
    print(f"La trucada té un import de: {calcul}")
else:
    calcul = (minuts) * (d)
    print(f"La trucada té un import de: {calcul}")