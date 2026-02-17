albumEspacos, albumCarimbadas, albumCompradas = input().split()
cromosCarimbados = [''] * int(albumCarimbadas)
cromosComprados = [''] * int(albumCompradas)

cromosCarimbadosDE = input().split()
for i in range(0, int(albumCarimbadas)):
    cromosCarimbados[i] = cromosCarimbadosDE[i]

cromosCompradosDE = input().split()
for i in range(0, int(albumCompradas)):
    cromosComprados[i] = cromosCompradosDE[i]

#print(cromosCarimbados)
#print(cromosComprados)

minhasCarimbadas = 0
for i in range(0, len(cromosCarimbados)):
    try:
        p = cromosComprados.index(cromosCarimbados[i])
        minhasCarimbadas += 1

    except ValueError:
        pass

print('%s' % str(int(albumCarimbadas)-minhasCarimbadas))
