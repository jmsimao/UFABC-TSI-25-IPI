from math import sqrt

varA, varB, varC = input().split()

varA = float(varA); varB = float(varB); varC = float(varC)

try:
    delta = pow(varB, 2) - (4 * varA * varC)

    if (delta < 0):
        print('nao ha raiz real')
    else:
        raiz1 = ((-1 * varB) + sqrt(delta)) / (2 * varA)
        raiz2 = ((-1 * varB) - sqrt(delta)) / (2 * varA)

        if (raiz1 == raiz2):
            print('%.4f' % (raiz1))
        else:
            print('%.4f %.4f' % (raiz1, raiz2))

except:
    print('nao ha raiz real')