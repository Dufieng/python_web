rychlost = int(input("Zadej rychlost: "))

if rychlost == 50:
    print("Jede v obci.")
elif 50 < rychlost <= 90:
    print("Jede mimo obec.")
elif 90 < rychlost <= 130:
    print("Jede po dálnici.")
else:
    print("Jede moc rychle!")
