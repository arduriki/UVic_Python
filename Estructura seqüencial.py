#Fer un programa que donats el radi i l’altura d’un cilindre en calculi la seva àrea i el seu volum:

print(" entra el radi:")
r=input()
r=float(r)
print("entra l'altura")
h=input() #height
h=float(h)
area=2*3.14*r**2+2*3.14*r*h #**vol dir elevat
volum=3.14*r**2*h
print(" àrea"+str(area))
print("volum"+str(volum))

#escurçat:

print("\n entra el radi:")#salt de linia: \n
r=float(input())
print("entra l'altura")
h=float(input())
a=2*3.14*r**2+2*3.14*r*h
v=3.14*r**2*h
print(" àrea"+str(a))
print("volum"+str(v))
