#Treure per pantalla els quadrats menors que 300 (1, 4, 9, 16...).

nombre = 1
calcul = 1

while calcul <= 300: #el tope és 17 dels quadrats menors a 300
    print(calcul)
    nombre = nombre + 1
    calcul = nombre ** 2 #actualitzacio del càlcul