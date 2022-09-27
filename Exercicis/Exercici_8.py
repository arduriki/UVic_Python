#Fer un programa que donats 3 valors numèrics d’entrada mostri quin és el més gran.

number1 = int(input("Write your first number: "))
number2 = int(input("Write your second number: "))
number3 = int(input("Write your third number: "))

if number1 > number2:
    if number1 > number3:
        print ("number1 is the highest number")
    elif number1 < number3:
        print ("number3 is the highest number")
    else:
        print ("number1 and number3 are equal")
elif number2 > number1:
    if number2 > number3:
        print ("number2 is the highest number")
    elif number2 < number3:
        print ("number3 is the highest number")
    else:
        print ("number2 and number3 are equal")
else:
    print ("number1 and number2 are equal")
