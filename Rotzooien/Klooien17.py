#Voer de namen van de teams in
naam_teamA = input("Voer naam team A in ")
naam_teamB = input("Voer naam team B in ")

#Bijhouden van de score per wedstrijd
score_teamA = []
score_teamB = []

#bijhouden punten gewonnen/ niet gewonnen (maximaal 4)
punten_teamA = 0
punten_teamB = 0

def score_per_wedstrijd():
    global punten_teamA, punten_teamB
    team_heeft_gewonnen = False
    wedstrijdnummer = 0

    while not team_heeft_gewonnen:
        wedstrijdnummer = wedstrijdnummer + 1
        print(f"Uitslag Wedstrijd {wedstrijdnummer}:")

        score_per_wedstrijd_teamA = int(input("geef het aantal punten voor team A in"))
        score_per_wedstrijd_teamB = int(input("geef het aantal punten voor team B in"))
        gewonnenstrijd(score_per_wedstrijd_teamA,score_per_wedstrijd_teamB)
        winnaar, team_heeft_gewonnen = printwinnaar(punten_teamA,punten_teamB,team_heeft_gewonnen)
        score_teamA.append(score_per_wedstrijd_teamA)
        score_teamB.append(score_per_wedstrijd_teamB)
        #Volgende kan eruit



        print(f"Kanweg: punten_teamA {punten_teamA}")
        print(f"Kanweg: punten_teamB {punten_teamB}")


def gewonnenstrijd(score_per_wedstrijd_teamA,score_per_wedstrijd_teamB):
    global punten_teamA, punten_teamB
    if score_per_wedstrijd_teamA>score_per_wedstrijd_teamB:
        punten_teamA = punten_teamA + 1
    else:
        punten_teamB = punten_teamB + 1


def printwinnaar(punten_teamA,punten_teamB,team_heeft_gewonnen):
    if punten_teamA == 4:
        winnaar = "Team A"
        team_heeft_gewonnen = True
        return winnaar, team_heeft_gewonnen

    elif punten_teamB ==4:
        winnaar = "Team B"
        team_heeft_gewonnen = True
        return winnaar, team_heeft_gewonnen
    else:
        return None



score_per_wedstrijd()





