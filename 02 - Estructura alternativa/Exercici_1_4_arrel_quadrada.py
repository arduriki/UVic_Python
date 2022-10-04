#Fer un programa que solucioni equacions de segon grau. Ha de comprovar que no hi ha arrels imaginàries i si n’hi ha mostrar un missatge d’avís.

print("Calculadora d'ecuacions de 2n grau")
a = float(input("Escriu el valor a: "))
b = float(input("Escriu el valor b: "))
c = float(input("Escriu el valor c: "))

eq = (b**2)-4*(a*c) #solució dintre arrel

if eq < 0:#número negatiu no hi ha solució.
    print("No existeix.")
else:
    eq = eq ** 0.5 #arrel quadrada
    x1 = (-b+eq) / 2
    x2 = (-b-eq) / 2
    print(f"x1 val {x1}")
    print(f"x2 val {x2}")