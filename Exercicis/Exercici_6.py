#Fer un programa que donat un any ens digui si és bixest. És bixest si es divisible per 4 i no per 100 o bé per 400

year = int(input("Which year do you want to check? "))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print ("Leap year.")
else:
    print ("Not leap year")
