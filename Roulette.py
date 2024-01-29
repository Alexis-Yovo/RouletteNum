import random

greenList = [0]
blackList = [2,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
redList = [1,3,5,7,9,12,14,13,18,19,21,23,25,27,30,32,34,36]

choiceNumber = int(input("Entrez un numéro : "))
number = random.randint(0,36)
print(number)

if(number in redList):
    print("Le numéro " + str(choiceNumber) + " correspond à une case rouge.")
elif(number in blackList):
    print("Le numéro " + str(choiceNumber) + " correspond à une case noire.")
else:
    print("Le numéro " + str(choiceNumber) + " correspond à une case verte.")

