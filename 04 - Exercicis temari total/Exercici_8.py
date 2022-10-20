#Donada una frase acabada en punt, determinar si té més lletres ‘b’ que ‘c’.

lletres = input("Escriu una frase lletra a lletra (acaba en punt): ")
count_b = 0
count_c = 0

while lletres != ".":
    if lletres == "b":
        count_b += 1
    elif lletres == "c":
        count_c += 1
    lletres = input("Escriu la següent lletra (acaba en punt): ")

if count_b > count_c:
    print("Hi ha més lletres b que c.")
elif count_b < count_c:
    print("Hi ha més lletres c que b.")
elif count_b == 0 and count_c == 0:
    print("No hi han lletres b i c.")
elif count_b == count_c:
    print("Hi han tantes lletres b que c.")