Gewicht = int(input("wat is uw gewicht afgerond naar kg "))
Lengte = float(input("wat is uw lengte in cm "))

print("Gewicht in kilogram: ", Gewicht)
print("Lengte in cm", Lengte)

BMI = float(Gewicht/(Lengte*Lengte))

if BMI >= 25:
    print("Er is sprake van overgewicht")
else:
    print("Je bent goed op gewicht")
