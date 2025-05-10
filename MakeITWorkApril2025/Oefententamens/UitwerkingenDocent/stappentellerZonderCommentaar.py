print("Dit programma is gemaakt door student X, MIW, 5008123456\n")

def bereken_kcal(aantalstappen):
    verbrande_calorieen = 0.03 * aantalstappen
    return verbrande_calorieen

minimum_stappen = int(input("Hoeveel stappen wil je minimaal lopen per dag? "))
while minimum_stappen < 5000:
    print("\tStel je doel hoger, minimaal 5000 stappen per dag!")
    minimum_stappen = int(input("Hoeveel stappen wil je minimaal lopen per dag? "))

dagen_van_de_week = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
gelopen_stappen_week = []

print("Voer het aantal stappen per dag in:")
for i in range(7):
    stappen_per_dag = int(input("\t%s: " % dagen_van_de_week[i]))
    gelopen_stappen_week.append(stappen_per_dag)

totaal_aantal_stappen = 0
for i in range(7):
    totaal_aantal_stappen = totaal_aantal_stappen + gelopen_stappen_week[i]

print("\nJe hebt deze week in totaal %d stappen gelopen." % totaal_aantal_stappen)
print("Je hebt hiermee %f kCal verbrand." % bereken_kcal(totaal_aantal_stappen))

print("Je hebt deze week te weinig stappen gelopen op: ", end="")
for i in range(7):
    if gelopen_stappen_week[i] < minimum_stappen:
        print(dagen_van_de_week[i], end=" ")

genoeg_stappen = True
for i in range(7):
    if gelopen_stappen_week[i] < minimum_stappen:
        genoeg_stappen = False

if genoeg_stappen:
    print("\nJe hebt alle dagen genoeg gelopen, ga zo door!")
