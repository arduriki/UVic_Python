#Fer un programa que donades 10 mesures fetes a laboratori ens digui quantes n’hi ha que estiguin entre l’ interval 0.9 i 1.

count = 0
interval = 0
measure = 0

while count < 10:
    measure = float(input("Write a measure number: "))
    if measure >= 0.9 and measure <= 1:
        interval = interval + 1
    count = count + 1
    
print(f"You have correct {interval} numbers")