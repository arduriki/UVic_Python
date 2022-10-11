#Calcular la mitjana de deu nombres teclejats.

nombres = 0
vegades = 0
mitjana = 10 #mitjana dels 10 nombres

while vegades <= mitjana:
    nombres = nombres + float(input("Escriu un número: "))
    vegades = vegades + 1
    
nombres = float(nombres / mitjana)
print(f"La mitjana dels 10 nombres teclejats és: {nombres}")