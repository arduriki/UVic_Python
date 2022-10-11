#Mostrar la suma dels nombre senars entre 1 i 1000

suma_total = int(0)
senar = int(1)#començo numero senar 1

while senar <= 999:#fins últim número senar fins a 1000
    suma_total = int(suma_total) + int(senar)
    senar = int(senar + 2)#sumo dos al primer senar

print (f"La suma total dels nombres senars entre 1 i 1000 és: {numero}")