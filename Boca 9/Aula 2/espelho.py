numA, numB = input().split()
numA = str(numA); numB = str(numB)
espelho = ""; output = "espelho"

for i in range(0, len(numB)):
    espelho+= numB[(len(numB)-i)-1]

if (espelho != numA):
    output = 'nao ' + output

print(output)