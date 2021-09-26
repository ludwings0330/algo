# Title : 장난감 동맹군
# Tag : 집합
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

TC = int(input())
while TC:
    TC -= 1
    N, M = map(int, input().split())

    pair = []

    for _ in range(M):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        pair.append([a, b])
    pair.sort()

    group_A = set()
    group_B = set()

    group_A.update([pair[0][0]])
    group_B.update([pair[0][1]])

    for i in range(1, N):
        a, b = pair[i]
        a = set([a])
        b = set([b])

        if a & group_A: # group_A에 이미 a가 있으니까, b는 무조건 b
            if b & group_A: # 근데 안에 이미 있으면? 탈락
                print('NO')
                break
            else:
                group_B.update(b)
                continue
        if a & group_B:
            if b & group_B:
                print('NO')
                break
            else:
                group_A.update(b)
                continue

        group_A.update(a)
        group_B.update(b)
    else:
        print('YES')
