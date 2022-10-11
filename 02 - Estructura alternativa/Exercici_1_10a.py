#Fer un programa que llegeixi un valor real (x) i en tregui un altre segons aquestes funcions:

x = int(input("Escriu el número x: "))

if x <= 0:
    fx = x**2 + 2
elif 0 < x and x < 2:
    fx = (3*x) + 1
else:
    fx = (x**2)-(4*x)+5

print(f"El resultat és {fx}")