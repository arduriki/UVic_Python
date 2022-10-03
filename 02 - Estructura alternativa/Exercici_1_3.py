#Sabent els minuts que dura, calcular l'import d'una trucada telefònica aplicant el següent criteri: si dura 3 minuts o menys, val 30 cèntims; si en dura més, compta una passa per minut des del primer moment. Una passa són quinze cèntims.
minuts = int(input("Benvingut/da a la calculadora de trucades.\n Quants minuts has passat en trucada? "))
primers_minuts = 0.3
minuts_passats = 0.15

if minuts <= 3:
    minuts = minuts * primers_minuts
    print(f"La trucada costa {minuts}€")
else:
    minuts = minuts * minuts_passats
    print(f"La trucada costa {minuts}€")