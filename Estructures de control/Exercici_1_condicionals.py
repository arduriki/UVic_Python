euros = int(input("Write how many euros you have: "))

if euros >= 500:
    remain = euros // 500 # dividir per enters -> //
    print("You have " + str(remain) + " five hundred euros note")
    euros = euros % 500 # residu de la divisio -> %
else:
    print("You have 0 five hundred euros note")
      
if euros >= 200:
    remain = euros // 200
    print("You have " + str(remain) + " two hundred euros note/s")
    euros = euros % 200
else:
    print("You have 0 two hundred euros note/s")

if euros >= 100:
    remain = euros // 100
    print("You have " + str(remain) + " one hundred euros note/s")
    euros = euros % 100
else:
    print("You have 0 one hundred euros note/s")

if euros >= 50:
    remain = euros // 50
    print("You have " + str(remain) + " fifty euros note/s")
    euros = euros % 50
else:
    print("You have 0 fifty euros note/s")

if euros >= 20:
    remain = euros // 20
    print("You have " + str(remain) + " twenty euros note/s")
    euros = euros % 20
else:
    print("You have 0 twenty euros note/s")

if euros >= 10:
    remain = euros // 10
    print("You have " + str(remain) + " ten euros note/s")
    euros = euros % 10
else:
    print("You have 0 ten euros note/s")

if euros >= 5:
    remain = euros // 5
    print("You have " + str(remain) + " five euros note/s")
    euros = euros % 5
else:
    print("You have 0 five euros note")

if euros >= 2:
    remain = euros // 2
    print("You have " + str(remain) + " two euros coin/s")
    euros = euros % 2
else:
    print("You have 0 two euros coin")


if euros >= 1:
    remain = euros // 1
    print("You have " + str(remain) + " one euros coin/s")
    euros = euros % 1
else:
    print("You have 0 one euros coin/s")
