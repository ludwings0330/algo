import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)
N = int(input())

isPrime = [True] * 999999
for n in range(2, len(isPrime)//2+1):
    if not isPrime[n]:
        continue

    k = 2
    while k * n <= len(isPrime)-1:
        isPrime[k*n] = False
        k += 1

cache = [[-1] * 1001 for _ in range(1001)]


def solve(left, right):
    if left == N and right == N:
        return 0

    if cache[left][right] != -1:
        return cache[left][right]

    tmp = 1 if isPrime[int(str(left) + str(right))] else 0
    cache[left][right] = 0
    if left < N:
        cache[left][right] = max(cache[left][right], solve(left+1, right) + tmp)
    if right < N:
        cache[left][right] = max(cache[left][right], solve(left, right+1) + tmp)

    return cache[left][right]


print(solve(1, 1) - 1)
