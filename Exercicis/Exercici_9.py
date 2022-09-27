#Fer un programa que donada una hora, un minuts i uns segons, li sumi un segon i retorni el resultat en format horari correcte. 
#Es dóna per fet que l'usuari introduirà bé les dades
hours = int(input("Write an hour figure in 24h format: "))
minutes = int(input("Write some minutes: "))
seconds = int(input("Write some seconds: ")) + 1
  
if seconds == 60:
    seconds=0
    minutes=minutes+1
    if minutes == 60:
        minutes=0
        hours=hours+1
        if hours == 24:
            hours=0
            print(str(hours)+":"+str(minutes)+":"+str(seconds))
        else:
            print(str(hours)+":"+str(minutes)+":"+str(seconds))
    else:
        print(str(hours)+":"+str(minutes)+":"+str(seconds))
else:
    print(str(hours)+":"+str(minutes)+":"+str(seconds))
