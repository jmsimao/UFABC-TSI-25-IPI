laco = True

def nomeMatricula(nomeEMatricula):
    nome = ''; matricula = ''; numeros = '0123456789'

    for i in range(0, len(nomeEMatricula)):
        if (numeros.find(nomeEMatricula[i]) == -1):
            nome += nomeEMatricula[i]
        else:
            matricula += nomeEMatricula[i]

    return [nome, matricula]

while (laco):
    try:
        nomeEMatricula = str(input())

        nome, matricula = nomeMatricula(nomeEMatricula)

        print('%s %s' % (nome, matricula))

    except EOFError:
        laco = False
        break
