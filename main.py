"""
#1
print("Jmeno?")
jmeno = input()
print("ahoj " + jmeno)

#2
print("cislo 1")
cislo1 = int(input())
print("cislo 2")
cislo2 = int(input())
print("soucet = "+ str(cislo1 + cislo2))

#3
print("slovo?")
print("pocet znaku: " +str(len(input())))
"""
#4
print("slovo 1")
slovo1 = len(input())
print("slovo 2")
slovo2 = len(input())
if(slovo1 > slovo2):
    print("slovo 1 je delsi")
elif(slovo1 == slovo2):
    print("slova jsou stejne dlouha")
else:
    print("slovo 2 je delsi")