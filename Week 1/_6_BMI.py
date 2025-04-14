#Naam: BMI berekening
#Doel: Bereken BMI op basis van gewicht (kg) en lengte in (cm)

gewicht_kg = int(input("Wat is uw gewicht in kg "))
lengte_cm = float(input("Wat is uw lengte in cm "))
lengte_mtr = lengte_cm/100

print("Gewicht in kilogram: ", gewicht_kg)
print("Lengte in mtr", lengte_mtr)

BMI = float(gewicht_kg/(lengte_mtr*lengte_mtr))

if BMI >= 25:
    print("Er is sprake van overgewicht.")
else:
    print("Je bent goed op gewicht.")
