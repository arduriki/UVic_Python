#Emetre una factura: donat un preu unitari i el nombre d'unitats comprades, aplicar un I.V.A. del 16% i també un descompte del 5% però només si l'import brut (preu total més I.V.A.) supera els 100 euros.

preu = float(input("Creador de factures.\n Quin és el preu del objecte? € "))
unitats = int(input("Quantes unitats s'emporten? "))

suma_pn = (preu) * (unitats)
pujada_iva = suma_pn * (16 / 100)
preu_iva = suma_pn + pujada_iva

if preu_iva >= 100:
    dte = preu_iva * (5/100) #dte 5%
    preu_iva = preu_iva - dte
    print(f"La factura és de: {preu_iva}€")
else:
    print(f"La factura és de: {preu_iva}€")