from math import sqrt
valores=input()
a=int(valores.split()[0])
b=int(valores.split()[1])
c=int(valores.split()[2])

delta = pow(b,2) - (4 * a * c)
x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)
print('%.4f %.4f' % (x1, x2))