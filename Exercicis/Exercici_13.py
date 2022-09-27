#Donada una seqüència com la del exercici 12, determinar quants productes s'han analitzat abans de trobar-ne dos de seguits amb qualitats AA.

qualitat = " "
qualitat_anterior = ""
producte = -2

while qualitat != "*" and not (qualitat == "A" and qualitat_anterior == "A"):
    producte = producte + 1
    qualitat_anterior = qualitat
    qualitat = input("Classifica el producte segons la seva qualitat: A, C, B, R: ")

if qualitat == "*":
    print("No hi ha doble A")
else:
    print(f"Hi ha {producte} productes analitzats")