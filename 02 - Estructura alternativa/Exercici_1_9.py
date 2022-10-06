#A la resta d'Europa, les qualificacions escolars són alfabètiques: la màxima és una "A", la següent una
#"B", i així fins a la "E". Podem establir una equivalència d'aquesta manera: "A" - 10, "B" - 8, "C" - 6, "D"
#- 4, "E" - 2. Fer un programa que donada una nota en format alfabètic la converteixi a numèric.

nota = input("Dóna la lletra de la nota de l'exàmen: ")

if nota == "A":
    print("La nota és d'un 10.")
elif nota == "B":
    print("La nota és un 8.")
elif nota == "C":
    print("La nota és un 6.")
elif nota == "D":
    print("La nota és un 4.")
elif nota == "E":
    print("La nota és un 2.")
else:
    print("Ho sento, no correspon a cap nota.")