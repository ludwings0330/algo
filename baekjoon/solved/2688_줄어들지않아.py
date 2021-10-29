T = int(input())

def solve(k, i):
    if i == n:
        return 1

    if cache[i][k] != -1:
        return cache[i][k]

    cache[i][k] = 0
    for nxt in range(k, 10):
        cache[i][k] += solve(nxt, i+1)
    return cache[i][k]

while T:
    T -= 1
    n = int(input())
    cache= [[-1] * 10 for _ in range(n)]
    print(solve(0, 0))