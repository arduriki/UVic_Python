#Donada una frase acabada en punt, dir quina és la primera vocal que hi apareix.

frase = input("Escriu una frase lletra a lletra: ")
primera_vocal = " "

while frase != "a" and frase != "e" and frase != "i" and frase != "o" and frase != "u" and frase != ".":
        frase = input("Continua escrivint: ")

if frase == ".":
    print("No hi ha primera vocal")
else:
    primera_vocal = (frase)
    print(f"La primera vocal és {primera_vocal}")