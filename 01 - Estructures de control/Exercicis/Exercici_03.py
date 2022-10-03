#suma +
#restar -
#multiplicar *
#dividir //
#print = imprimir
#input = usuari@ introduzca un valor

#1.013hPa
#0.760mm Hg

#1hPa = 0.76mm Hg


#Fer un programa que donada una mesura en mil·límetres de mercuri els passi a hectoPascals. (1013 hPa=760mm Hg)
data_mercury = float(input("How many mercury mm you have? "))
hpa = (data_mercury * 1013) / 760
print("You have " + str(hpa) + " hPa")
