def test(m,n):
    for i in range(m):
        print(m, end="")
        for j in range(n):
            print(n,end="")
        print()

m= int(input("Geef de hoogte met m: "))
n= int(input("Geef de breedte met n: "))

test(m,n)
