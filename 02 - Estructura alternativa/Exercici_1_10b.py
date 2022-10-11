#Fer un programa que llegeixi un valor real (x) i en tregui un altre segons aquestes funcions:

x = float(input("Escriu el número x: "))

if x == 0:
    fx = 1
elif -1 <= x and x <= 1:
    fx = x**2
else:
    fx = x**0.5

print(f"El resultat és {fx}")