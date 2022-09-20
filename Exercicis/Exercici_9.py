#Fer un programa que donada una hora, un minuts i uns segons, li sumi un segon i retorni el resultat en format horari correcte. 
#Es dóna per fet que l'usuari introduirà bé les dades

seconds = int(input("Write some seconds: ")) + 1
minutes = int(input("Write some minutes: "))
hours = int(input("Write an hour figure in 24h format: "))
  
if seconds >= 60:
    minutes = minutes+1
    seconds = 0

if minutes >= 60:
    hours = hours+1
    minutes = 0

if hours >=24:
    hours = 0

print("The time is "+str(hours)+":"+str(minutes)+":"+str(seconds))
