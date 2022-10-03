#Fer un programa que ens retorni el valor absolut d’un número

num = float(input("Write a number in order to know its absolute value: "))

if num < 0:
    num = (num * -1)
    print(str(num) + " is the absolute value")
else:
    print(str(num) + " is the absolute value")
