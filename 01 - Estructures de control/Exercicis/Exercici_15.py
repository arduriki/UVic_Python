#Donada una seqüència de 10 valors com la de l'exercici 13, comptar quantes vegades apareix la seqüència RBA.
count = 0
val1 = " "
val2 = " "
val3 = " "
secuence = 0

while count < 10:
    if val3=="R" and val2=="B" and val1=="A":
        secuence = secuence + 1
    val3 = val2
    val2 = val1
    val1 = input("Write the quality of the product A, C, B, R: ")
    count = count + 1
    
print(f"You have {secuence} RBA secuences")