import sys
input = lambda: sys.stdin.readline()


def lis(i):
    if cache[i] != -1:
        return cache[i]

    cache[i] = 1
    best_nxt = -1
    for nxt in range(i+1, N+1):
        if A[i] < A[nxt]:
            candidate = lis(nxt) + 1
            if candidate > cache[i]:
                cache[i] = candidate
                best_nxt = nxt
    choices[i] = best_nxt
    return cache[i]


def reconstruct(start):
    if start != 0:
        seq.append(A[start])
    nxt = choices[start]
    if nxt != -1: reconstruct(nxt)


N = int(input())
A = [-float('inf')] + list(map(int, input().split()))

cache = [-1] * (N+1)
choices = [-1] * (N+1)
seq = []

print(lis(0) - 1)
print(choices)
reconstruct(0)
print(seq)