# 최소 한개의 모음 (a, e, i, o, u)
# 최소 두개의 자음
import sys
input = sys.stdin.readline

V = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())

alphas = list(input().split())
alphas.sort()
pw = []

def recursive(i, v, c , toPick):
    if toPick == 0:
        if v >= 1 and c >= 2:
            print(''.join(pw))
        else:
            return

    for i in range(i, len(alphas)):
        if alphas[i] in V:
            tv = v+1
            tc = c
        else:
            tv = v
            tc = c+1

        pw.append(alphas[i])
        recursive(i+1, tv, tc, toPick-1)
        pw.pop()

    pass

recursive(0, 0, 0, L)