#Fer un programa que donades dues temperatures ens digui quina és la més alta.

temp1 = float(input("Write a first temperature in celsius: "))
temp2 = float(input("Write a second temperature in celsius: "))

if temp1 > temp2:
    print (str(temp1)+" is higher than "+str(temp2))
else:
    print (str(temp1)+" is lower than "+str(temp2))
