#Operadors:
# // -> Dividir
# % -> Residu de la divisio (en aquest cas sería el restant dels diners)

euros = int(input("Write how many euros you have: ")) #variable d'entrada

note500 = euros // 500 #divideix la quantitat d'euros per 500
print("You have " + str(note500) + " five hundred euros note/s")
euros = euros % 500 #euros que queden

note200 = euros // 200
print("You have " + str(note200) + " two hundred euros note/s")
euros = euros % 200

note100 = euros // 100
print("You have " + str(note100) + " one hundred euros note/s")
euros = euros % 100

note50 = euros // 50
print("You have " + str(note50) + " fifty euros note/s")
euros = euros % 50

note20 = euros // 20
print("You have " + str(note20) + " twenty euros note/s")
euros = euros % 20

note10 = euros // 10
print("You have " + str(note10) + " ten euros note/s")
euros = euros % 10

note5 = euros // 5
print("You have " + str(note5) + " five euros note/s")
euros = euros % 5

coin2 = euros // 2
print("You have " + str(coin2) + " two euros coin/s")
euros = euros % 2

coin1 = euros // 1
print("You have " + str(coin1) + " one euros coin/s")
