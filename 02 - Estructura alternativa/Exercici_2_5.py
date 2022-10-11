#Mostrar la sumar dels nombre senars i la suma dels nombres parells entre 1 i 1000

suma_senar = int(0)
senar = int(1)#començo numero senar 1
suma_parell = int(0)
parell = int(2)#començo numero parell 2

while senar != 999 and parell != 1000: #els dos topes de senars i parells
    suma_senar = int(suma_senar) + int(senar)
    senar = int(senar + 2)#sumo dos al primer senar
    suma_parell = int(suma_parell + int(parell))
    parell = int(parell + 2)

print (f"La suma total dels nombres senars entre 1 i 1000 és: {suma_senar}")
print (f"La suma total dels nombres parells entre 1 i 1000 és: {suma_parell}")