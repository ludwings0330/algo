C = int(input())


def JLIS(startA, startB):
    # 메모이제이션
    if cache[startA + 1][startB + 1] != -1 :
        return cache[startA + 1][startB + 1]

    cache[startA + 1][startB + 1] = 2
    a = -float('inf') if startA == -1 else A[startA]
    b = -float('inf') if startB == -1 else B[startB]
    MAX = max(a, b)
    for nextA in range(startA+1, nA):
        if startA == -1 or MAX < A[nextA]:
            cache[startA+1][startB+1] = max(cache[startA+1][startB+1], JLIS(nextA, startB) + 1)

    for nextB in range(startB+1, nB):
        if startB == -1 or MAX < B[nextB]:
            cache[startA + 1][startB + 1] = max(cache[startA+1][startB+1], JLIS(startA, nextB) + 1)

    return cache[startA + 1][startB + 1]

for testCase in range(1, C+1):
    nA, nB = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cache = [[-1] * (nB + 1) for _ in range(nA + 1)]

    print(JLIS(-1, -1) - 2)