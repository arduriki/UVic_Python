#Fer un programa que donada una seqüència de temperatures acabada en 0, ens digui quantes n’hi ha de positives.

correct = 0
t = float(input("Write a temperature: "))

while t != 0:
    if t >= 1:
        correct = correct + 1
    t = float(input("Write a temperature: "))
        
print(f"You have {correct} positive temperatures")