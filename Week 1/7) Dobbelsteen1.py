from xml.dom.minidom import ElementInfo

aantalogen = int(input("Voer een getal tussen 1 en 6: "))

if aantalogen <1 or aantalogen >6:
    print("Ongeldige worp")
if aantalogen == 1:
    print("#")
elif aantalogen == 2:
    print("# #")
elif aantalogen == 3:
    print("# # #")
elif aantalogen == 4:
    print(" # #\n","# #")
elif aantalogen == 5:
    print(" # #\n"," # \n","# #")
elif aantalogen == 6:
    print(" # # # \n","# # #")


