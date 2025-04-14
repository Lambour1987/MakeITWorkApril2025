# Gemiddelde
# Door Maarten Lambour
# Bereken het gemiddelde van minimaal 2 getallen

#recursief of iteratief

def eerste_getallen():
    eerste_getal = int(input("Geef het eerste getal "))
    tweede_getal = int(input("Geef het tweede getal "))

def vraag():
    antwoord = input("Wil je van meer getallen het gemiddelde bepalen? (ja/nee)")

    if antwoord == 'ja':
        volgende_getallen()
    elif antwoord == 'nee':
        bereken_gemiddelde()
    else:
        print("Onjuist gegeven")


def volgende_getallen()


def bereken_gemiddelde()


aantal = int(input("geef aantal "))
totaal = 0

for i in range(aantal):
    getal = int(input("geef getal: "))
    totaal = getal + totaal
    print(totaal)
    i = i+1
gemiddelde = totaal/aantal

print(gemiddelde)

def main():
    eerste_getallen()


