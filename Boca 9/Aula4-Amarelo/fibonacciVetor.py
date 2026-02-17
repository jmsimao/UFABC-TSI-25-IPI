casosDeTeste = int(input())
i = 0

def fibonacci(n):
    i = 1
    if (n == 0):
        r = 0
    #elif (n <= 2):
    #    r = 1
    else:
        ant = 0; i = 1; r = 0
        for p in range(1, n+1):
            #print('n %d' % p)
            r = ant + i; r = 1 if (r == 0) else r
            i = ant; ant = r
            #print('f(%d) -> %d' % (p, r))

  #         c    ant < r    ant > i   r
  #         1    0                0   1
  #         2    0     1    0     0   1
  #         3    1     1    1     1   2
  #         4    1     2    1     1   3
  #         5    2     3    2     2   5
  #         6    3     5    3     3   8
  #         7    5     8    5     5  13
  #         8    8    13    8     8  21

    return r


while (i < casosDeTeste):
    try:
        enesimo = int(input())
        f = fibonacci(enesimo)
        print('Fib(%d) = %d' % (enesimo, f))

        i += 1

    except EOFError:
        break
