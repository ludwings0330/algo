N, M, K = map(int, input().split())
# N개의 x, M개의 y로 이루어진 사전에서, K 번째 문자열을 구해라.
cache = [[-1] * (M+1) for _ in range(N+1)]

def solve(x, y):
    if x == 0 and y == 0:
        return 1

    if cache[x][y] != -1:
        return cache[x][y]

    cache[x][y] = 0
    if x > 0:
        cache[x][y] += solve(x-1, y)
    if y > 0:
        cache[x][y] += solve(x, y-1)

    return cache[x][y]

def get_ans(n, m, k):
    if n == 0 or m == 0 or k == 0:
        return 'a' * n + 'z' * m

    if k <= cache[n-1][m]:
        return "a" + get_ans(n-1, m, k)
    else:
        return "z" + get_ans(n, m-1, k - cache[n-1][m])

solve(N, M)
ans = ""
if cache[N][M] < K:
    print(-1)
else:
    print(get_ans(N, M, K))
