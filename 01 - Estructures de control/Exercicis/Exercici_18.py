#Es demana fer un programa que rebi una seqüència d’humitats i ens retorni quina és la primera humitat que té un valor inferior a la primera llegida.

h1 = float(input("Write a humidity number: "))
h = float(input("Write a humidity number: "))

while h >= h1 and h!= 0:
    h = float(input("Write a humidity number: "))

if h == 0:
    print(f"You haven't given me a number lesser than the first figure")
else:
    print(f"{h} is less than the first figure {h1}")