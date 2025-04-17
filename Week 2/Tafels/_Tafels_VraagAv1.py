tafel = int(input("Welke tafel wilt u printen?: "))
tot_aan = int(input("Tot hoever wil je door?: "))

totaal = 0
i = 0

while i<tot_aan:
    i = i + 1
    totaal = i * tafel
    print(i,"*",tafel,'=',totaal)