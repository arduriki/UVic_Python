#Fer un programa que donat un valor de x retorni el valor f(x) per la funció: x/x-2  si  f(x) =  x2-4  si  2x/x-5  si  x < 2 2 <= x <= 5 x > 5

x = int(input("Write a number: "))

if x < 2:
    fx = int(x / x - 2)

elif 2 <= x or x <= 5:
    fx = int(x**2 - 4)

else:
    fx = int((2**x) / (x - 5))

print("f(x) is " + str(fx))
