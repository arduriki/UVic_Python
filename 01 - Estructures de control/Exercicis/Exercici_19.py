#Es demana fer un programa que demani d’entrada un llindar de pol·lució de partícules en suspensió i després l’entrada de la pol·lució a VIC durant 30 dies i ens retorni quants dies ha estat per sobre del llindar.

th1 = float(input("Set the minimal figure to set a polution threshold: ")) 
th2 = float(input("Set the maximum figure to set a polution threshold: ")) #posa el tope del llindar
days = 0
measure = float(0.0)
outside = 0

while days < 5: #dies fins que arribi a 5
    days = days + 1 #compte els dies
    measure = float(input(f"Today is day {days}. Write today's measure: ")) #demana la mesura del dia
    if measure <= th1 or measure >= th2: #fora del llindar
        outside = outside + 1 #quants queden fora del llindar
    
    
print(f"This month we had {outside} days outside the threshold.")