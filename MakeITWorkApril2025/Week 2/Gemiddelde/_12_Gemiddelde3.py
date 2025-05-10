
def gemiddelde():

    getal_1 = int(input("Dit programma berekent het gemiddelde van twee of meer getallen. \nGeef het eerste getal: "))
    getal_2 = int(input("Geef het tweede getal: "))

    while True:
        antwoord = str(input("Wil je van meer getallen het gemiddelde bepalen? (ja/nee): "))
        antwoord = antwoord.lower()
        aantal_getallen = 2
        huidige_som = getal_1 + getal_2

        if antwoord == "ja":
            aantal_getallen = aantal_getallen + 1
            getal_volgende = int(input("Geef het volgende getal: "))
            huidige_som = huidige_som + getal_volgende

        elif antwoord == "nee":
            gemiddelde = huidige_som / aantal_getallen
            return gemiddelde,aantal_getallen
        else:
            print("Je moet 'ja' of 'nee' antwoorden.")


berekend_gemiddelde,aantal_getallen = gemiddelde()
print(f"Het gemiddelde van jouw {aantal_getallen} getallen is {berekend_gemiddelde}")

