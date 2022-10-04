#Fer un programa que, donada una hora en format hores, minuts i segons, li sumi un segon.

hours = int(input("Write an hour figure in 24h format: "))
minutes = int(input("Write some minutes: "))
seconds = int(input("Write some seconds: ")) + 1 #sumem el segon
  
if seconds >= 60:
    seconds = 0
    minutes = minutes + 1 #si segons arriben a 60, li suma 1 als minuts
    if minutes >= 60:
        minutes = 0
        hours = hours + 1 #si minuts arriben a 60, li suma 1 a les hores
        if hours >= 24:
            hours = 0
            print(f"{hours}:{minutes}+{seconds})
        else:
            print(f"{hours}:{minutes}+{seconds})
    else:
        print(f"{hours}:{minutes}+{seconds})
else:
    print(f"{hours}:{minutes}+{seconds})