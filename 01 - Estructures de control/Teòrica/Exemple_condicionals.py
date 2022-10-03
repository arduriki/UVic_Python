#exemple de condicionals
#Donada una seqüència de valor acabat en zero, calcular la seva suma

suma = 0
num = int(input("Write a number: "))
while num != 0: #quan l'usuari prem el 0, s'acabarà el bucle
    suma = suma + num #sumem el número a la variable i el va acumulant
    num = int(input("Write a number: "))
print (suma)
