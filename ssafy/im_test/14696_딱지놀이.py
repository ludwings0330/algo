# 별 > 동그라미 > 네모 > 세모
from collections import defaultdict

N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    store_a = defaultdict(int)
    store_b = defaultdict(int)

    for shape in A[1:]:
        store_a[shape] += 1

    for shape in B[1:]:
        store_b[shape] += 1

    winner = 0
    for shape in range(4, 0, -1):
        if store_a[shape] > store_b[shape]:
            winner = 1
            break
        elif store_a[shape] < store_b[shape]:
            winner = 2
            break
    if winner == 0:
        print("D")
    elif winner == 1:
        print("A")
    else:
        print("B")