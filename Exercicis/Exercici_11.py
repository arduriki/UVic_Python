#Fer un programa que donada una seqüència d’anys acabada en 0 ens digui quants n’hi ha del segle 20.

year=int(input("Write a 20th century year: "))
correct=0

while year != 0:
    if year <= 1900 and year >= 2001:
        year = int(input("Wrong! Write a 20th century year: "))
    else:
        correct = correct + 1
        year=int(input("Write a 20th century year: "))

print(f"You have written {correct} 20th century years")
