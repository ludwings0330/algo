import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n0, n1, n2 = map(int, input().split())
    s = []
    if n0 > 0:
        s.extend(['0'] * (n0 + 1))
    if n2 > 0:
        s.extend(['1'] * (n2 + 1))
    if n1 > 0:
        if n0 > 0 and n2 > 0:
            n1 -= 1
        if n0 == 0 and n2 == 0:
            s.append('1')
        for _ in range(n1):
            if s[-1] == '0':
                s.append('1')
            else:
                s.append('0')

    print(''.join(s))

