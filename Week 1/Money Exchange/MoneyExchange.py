
# Koers 15-4-2025
#1 EURO = 161,60 yen
#1 EURO = 1,13 dollar
#1 EURO = 0.8554 pond

EURO_YEN = 161      # Yen
EURO_DOLLAR = 1.13     # Dollar
EURO_POND = 0.8554   # Pond

valuta = int(input("1=US dollar, 2=GB pounds, 3=Yen "))
vreemd_bedrag = int(input("In te wisselen bedrag (gehele getallen): "))

if valuta == 1:
    eur_bedrag = float(vreemd_bedrag/EURO_DOLLAR)
elif valuta == 2:
    eur_bedrag = vreemd_bedrag/EURO_POND
elif valuta == 3:
    eur_bedrag = vreemd_bedrag/EURO_YEN
else:
    print("onjuist ingevoerd")

print(f"Voor {vreemd_bedrag}{valuta} krijgt u {eur_bedrag}{valuta}")






