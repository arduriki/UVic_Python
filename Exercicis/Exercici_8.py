#Fer un programa que donats 3 valors numèrics d’entrada mostri quin és el més gran.

number1 = int(input("Write your first number: "))
number2 = int(input("Write your second number: "))
number3 = int(input("Write your third number: "))

if number1 < number2 < number3:
    print("Biggest number is: " + str(number3))
elif number1 < number2 > number3:
    print("Biggest number is " + str(number2))
else:
    print("Biggest number is " + str(number1))
