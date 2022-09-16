euros = int(input("Write how many euros you have: "))

euros500 = euros // 500
print("You have " + str(euros500) + " five hundred euros note/s")
euros = euros % 500

euros200 = euros // 200
print("You have " + str(euros200) + " two hundred euros note/s")
euros = euros % 200

euros100 = euros // 100
print("You have " + str(euros100) + " one hundred euros note/s")
euros = euros % 100

euros50 = euros // 50
print("You have " + str(euros50) + " fifty euros note/s")
euros = euros % 50

euros20 = euros // 20
print("You have " + str(euros20) + " twenty euros note/s")
euros = euros % 20

euros10 = euros // 10
print("You have " + str(euros10) + " ten euros note/s")
euros = euros % 10

euros5 = euros // 5
print("You have " + str(euros5) + " five euros note/s")
euros = euros % 5

euros2 = euros // 2
print("You have " + str(euros2) + " two euros coin/s")
euros = euros % 2

euros1 = euros // 1
print("You have " + str(euros2) + " one euros coin/s")
