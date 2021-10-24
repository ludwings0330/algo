import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [float(input()) for _ in range(N)]

cache = [-1] * (N + 1)

def MMS(n):
    if n == N:
        return 1

    if cache[n] != -1:
        return cache[n]

    cache[n] = max(arr[n], arr[n] * MMS(n+1))
    return cache[n]

MMS(0)
print("%.3f" %max(cache))