alunos = int(input()); pizza6 = int(input()); pizza4 = int(input())

def pizza(a, p8, p6):
    sobra = 0 if (((p8 * 8)+(p6 * 6) - a) < 0) else (((p8 * 8) + (p6 *6)) - a)

    return sobra

print('%d' % pizza(alunos, pizza6, pizza4))
