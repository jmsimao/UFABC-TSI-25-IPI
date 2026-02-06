soma = 0
infinito = True

while (infinito):
    try: 
        numero = input() 

        if numero == "":
            infinito = False
        else:
            soma += int(numero)
    
    except:
        infinito = False 
    
print(soma)