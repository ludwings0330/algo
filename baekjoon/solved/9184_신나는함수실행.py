L = 101
dp = [[[0]*L for i in range(L)] for j in range(L)]
# (50 - a)
def w(a, b, c):
    p, q, r = 50-a, 50-b, 50-c
    if a <= 0 or b <= 0 or c <= 0:
        dp[p][q][r] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        if dp[p][q][r] == 0:
            dp[p][q][r] = w(20, 20, 20)
        return dp[p][q][r]
    elif a < b and b < c:
        if dp[p][q][r+1] == 0:
            dp[p][q][r+1] = w(a, b, c-1)
        if dp[p][q+1][r+1] == 0:
            dp[p][q+1][r+1] = w(a, b-1, c-1)
        if dp[p][q+1][r] == 0:
            dp[p][q+1][r] = w(a, b-1, c)
        return dp[p][q][r+1] + dp[p][q+1][r+1] - dp[p][q+1][r]
    else:
        if dp[p+1][q][r] == 0:
            dp[p + 1][q][r] = w(a-1, b, c)
        if dp[p+1][q+1][r] == 0:
            dp[p + 1][q + 1][r] = w(a-1, b-1, c)
        if dp[p+1][q][r+1] == 0:
            dp[p + 1][q][r + 1] = w(a-1, b, c-1)
        if dp[p+1][q+1][r+1] == 0:
            dp[p + 1][q + 1][r + 1] = w(a-1, b-1, c-1)
        return dp[p + 1][q][r] + dp[p+1][q+1][r] + dp[p+1][q][r+1] - dp[p+1][q+1][r+1]

while True:
    a, b, c = map(int, input().split())

    if a == b == c == -1:
        break
    else:
        print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))