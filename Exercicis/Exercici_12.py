#Un procés de control de qualitat per visio classifica els productes en A(qualitat extra), C(correcte), B(qualitat baixa), R(rebutjar). Fer un programa que va rebent la qualitat resultant dels productes analitzats fins a rebre un * i determini quantes vegades la classificació ha estat R.

qualitat = input("Classifica el producte segons la seva qualitat A, C, B, R: ")
rebutjat = int(0)

while qualitat != "*":
    if qualitat == "R":
        rebutjat = rebutjat + 1
    qualitat = input("Classifica el producte segons la seva qualitat A, C, B, R: ")

print(f"Tens {rebutjat} productes rebutjats")
