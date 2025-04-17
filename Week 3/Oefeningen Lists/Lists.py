
# Range en lists
for i in range(0,10,1):
    print(i)
print('\n')

for i in range(1,11,1):
    print(i)
print('\n')

for i in range(2,12,2):
    print(len(i))

#Rij van random getallen

def random():
    totaal_aantal = int(input("Hoeveel getallen wil je genereren"))
    aantal = 0

    while aantal <= totaal_aantal:
        print(random(0, aantal))
        aantal = aantal + 1
