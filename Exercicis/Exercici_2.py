#dades (números / text) bàsiques
#enter: int
#reals (amb coma .): float
#cadenes de text: str
#input
#print
#assignacio: símbol =

celsius = float(input("Write the temperature in Celsius: "))
fahrenheit = celsius*1.8+32
kelvin = celsius+273

print("Your temperature in Fahrenheit is: " + str(fahrenheit)+ " ºF")
print("Your temperature in Kelvin is: " + str(kelvin) + " ºK")
