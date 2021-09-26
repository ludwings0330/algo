MAX = 10**6

K, L = map(int, input().split())

flag = True
for i in range(2, L):
    if K%i == 0:
        flag ^= True
        break

if flag:
    print('GOOD')
else:
    print('BAD {0}'.format(i))
