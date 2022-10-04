#Llegir tres nombres i escriure el major.

print("Quin és el número més gran?")
a = float(input("Introdueix el primer numero: "))
b = float(input("Introdueix el segon numero: "))
c = float(input("Introdueix el tercer numero: "))

if a > b and a > c:
    print(f"El numero {a} és el més gran")
elif b > a and b > c:
    print(f"El numero {b} és el més gran")
elif c > a and c > b:
    print(f"El numero {c} és el més gran")
elif a == b > c:
    print(f"Els numeros {a} i {b} són els més grans")
elif a == c > b:
    print(f"Els numeros {a} i {c} són els més grans")
elif b == c > a:
    print(f"Els numeros {b} i {c} són els més grans")
else:
    print("Els tres numeros són iguals")