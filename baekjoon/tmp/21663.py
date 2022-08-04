import sys

input = lambda: sys.stdin.readline().rstrip()
while True:
    N = int(input())

    f = list(input())
    if f[2] == '1':
        print('1' + '0' * (N-1))
    elif f[3] == '1':
        print('1' * N)
    elif f[1] == '1':
        print('1' * (N-2) + '01')
    elif f[0] == '1':
        if N == 2:
            print('00')
        else:
            print('1' * (N-1) + '0')
    else:
        print('No solution')