#Escriure els N primers múltiples de M (N i M són valors introduïts per l’usuari)

m = int(input("Quin número vols saber els seus múltiples? "))
n = int(input("Quants multiples vols? "))
vegades = 0
multiples = 2 #començo a multiplicar per 2.

while vegades != n:
    m_multiple = m * multiples
    print(m_multiple)
    multiples = multiples + 1
    vegades = vegades + 1