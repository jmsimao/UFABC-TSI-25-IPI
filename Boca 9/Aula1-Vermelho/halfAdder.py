booleans = input().split()

bool1 = 0 if booleans[0] == 'false' else 1
bool2 = 0 if booleans[1] == 'false' else 1

ret = ''

if (bool1 == 0 and bool2 == 0):
    ret = 'false false'
elif (bool1 == 0 and bool2 == 1):
    ret = 'false true'
elif (bool1 == 1 and bool2 == 0):
    ret = 'false true'
elif (bool1 == 1 and bool2 == 1):
    ret = 'true false'

print('%s' % ret)
