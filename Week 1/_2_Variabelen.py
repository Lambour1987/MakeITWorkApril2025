#Variabelen door Maarten Lambour
#Doel: Afdrukken van achternaam en het berekenen van de Leeftijd en het gemiddelde van de temperatuur van vandaag en gisteren


achternaam = input("Wat is je achternaam? ")
leeftijd = int(input("Wat is je leeftijd? "))
tempvandaag = 23.1
tempgisteren = 25.6
tempgem = float((tempvandaag+tempgisteren)/2)

print("Je achternaam is", achternaam)
print("Je leeftijd over 10 jaar is", leeftijd + 10)
print(tempgem)

