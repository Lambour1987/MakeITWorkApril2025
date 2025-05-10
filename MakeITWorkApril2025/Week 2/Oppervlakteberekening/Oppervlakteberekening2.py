#Oppervlakteberekening door Maarten Lambour
#Berekenen van de oppervlakte van een cirkel, rechthoek, vierkant en driehoek


import math


def cirkel():
    straal = int(input("Wat is de straal in cm?"))
    PI = 3.14
    oppervlakte = straal * straal * PI
    print(f"De oppervlakte van jouw cirkel is {oppervlakte} vierkante cm.")

def rechthoek():
    hoogte_cm = int(input("Wat is de hoogte in cm? "))
    breedte_cm = int(input("Wat is de breedte in cm? "))
    oppervlakte = hoogte_cm * breedte_cm
    print(f"De oppervlakte van jouw rechthoek is {oppervlakte} vierkante cm.")

def vierkant():
    zijde = int(input("Wat is de zijde in cm?"))
    oppervlakte = math.pow(zijde,2)
    print(f"De oppervlakte van jouw vierkant is {oppervlakte} vierkante cm.")

def driehoek():
    basis_cm = int(input("Wat is de basis in cm? "))
    hoogte_cm = int(input("Wat is de hoogte in cm? "))
    oppervlakte = (hoogte_cm * basis_cm)/2
    print(f"De oppervlakte van jouw driehoek is {oppervlakte} vierkante cm.")



keuze_figuur = int(input(
    "Van welke figuur wil je de oppervlakte uit laten rekenen? \n(cirkel = 1; rechthoek = 2; vierkant = 3; driehoek = 4; stoppen = 0): "))

while keuze_figuur != 0:
    if keuze_figuur == 1:
        cirkel()
    elif keuze_figuur == 2:
        rechthoek()
    elif keuze_figuur == 3:
        vierkant()
    elif keuze_figuur == 4:
        driehoek()
    else:
        print("Ongeldige keuze, probeer opnieuw")

    keuze_figuur = int(input("Van welke figuur wil je NU de oppervlakte uit laten rekenen? \n(cirkel = 1; rechthoek = 2; vierkant = 3; driehoek = 4; stoppen = 0): "))
print("Het programma wordt nu gestopt")
