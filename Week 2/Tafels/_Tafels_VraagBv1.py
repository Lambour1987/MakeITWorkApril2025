tafel = int(input("Welke tafel wilt u printen?: "))
tot_aan = int(input("Tot hoever wil je door?: "))

totaal = 0
i = 0

print(f"De tafel van {tafel}:")

for i in range(0,10):
    print(i, end='')
    for j in range (0,10):
        i = i + 1
        totaal = i * tafel
        print(totaal, end = "  ")