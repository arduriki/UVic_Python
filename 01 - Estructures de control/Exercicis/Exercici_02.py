#dades (números / text) bàsiques
#enter: int
#reals (amb coma .): float
#cadenes de text: str
#input
#print
#assignacio: símbol =

#Fer un programa que donada una temperatura en graus Celsius en la mostri en graus Fahrenheit i en graus Kelvin. (F = 1.8C + 32 i K = C + 273)

celsius = float(input("Write the temperature in Celsius: "))
fahrenheit = celsius*1.8+32
kelvin = celsius+273

print("Your temperature in Fahrenheit is: " + str(fahrenheit)+ " ºF")
print("Your temperature in Kelvin is: " + str(kelvin) + " ºK")
