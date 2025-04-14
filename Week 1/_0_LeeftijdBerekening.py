""""
Dit programma heeft tot doel de leeftijd te berekenen van
de gebruiker te berekenen en een boodschap te geven afhankelijk
van zijn leeftijd. Gemaakt door Maarten Lambour
"""

JAAR = 2025

#Deze functie berekent de leeftijd o.b.v. het geboortejaar
def ber_leeftijd(JAAR, geboortejaar):
    leeftijd = JAAR-geboortejaar
    return leeftijd

#Deze functie bepaalt een boodschap o.b.v. de leeftijd
def boodschap_leeftijd(leeftijd):
    if leeftijd >= 50:
        boodschap = "Ondank je leeftijd zie je er nog best goed uit!"
    else:
        boodschap = "Je bent nog lang niet toe aan pensioen."
    return boodschap

#De hoofdfunctie drukt het resultaat af van de leeftijd en boodschap
def main():
    voornaam = input("Hoe heet je? ")
    geboortejaar = int(input("Wat is je geboortejaar? "))
    leeftijd = ber_leeftijd(JAAR, geboortejaar)
    print(f"Beste {voornaam}, in {JAAR+10} zal je leeftijd {leeftijd+10} zijn")
    boodschap = boodschap_leeftijd(leeftijd)
    print(boodschap)


if __name__ == "__main__":
    main()

