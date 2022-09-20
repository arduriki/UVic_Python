#Fer un programa que donat un valor de x retorni el valor f(x) per la funció: x/x-2  si  f(x) =  x2-4  si  2x/x-5  si  x < 2 2 <= x <= 5 x > 5

number_given = int(input("Write a number: "))

if number_given < 2:
    fx = number_given // number_given - 2

if 2 <= number_given <= 5:
    fx = number_given * 2 - 4

if number_given > 5:
    fx = 2 * number_given / number_given - 5

print("f is " + str(fx))
