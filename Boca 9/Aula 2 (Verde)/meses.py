meses = ['JANEIRO','FEVEREIRO','MARCO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO','MES INVALIDO']

entrada = int(input())

if (entrada <= 0 or entrada > len(meses)):
    print(meses[12])
else:
    print(meses[entrada-1])