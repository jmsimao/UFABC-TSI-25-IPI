altura, peso = input().split()
desc =  ['Magreza grave','Magreza moderada','Magreza leve','Saudavel','Sobrepeso',
        'Obesidade Grau I','Obesidade Grau II (severa)','Obesidade Grau III (morbida)']

altura = float(altura); peso = float(peso)
imc = (peso / pow(altura, 2))

if (imc < 16 ):
    ret = 0
elif (imc >= 16  and imc < 17):
    ret = 1
elif (imc >= 17  and imc < 18.5):   
    ret = 2
elif (imc >= 18.5  and imc < 25):   
    ret = 3
elif (imc >= 25  and imc < 30):   
    ret = 4
elif (imc >= 30  and imc < 35):   
    ret = 5
elif (imc >= 35  and imc < 40):   
    ret = 6
else:
    ret = 7

print('%s' % desc[ret])