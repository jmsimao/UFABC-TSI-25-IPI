laco=True; soma=0; literais = 'aeiou'

while (laco):

    try:
        letra = str(input())
     
        if (letra == '*'):
            laco = False
        else:
            letra = letra.lower()

            if (letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u'):
                soma += 1

    except EOFError:
        laco = False

print(soma)