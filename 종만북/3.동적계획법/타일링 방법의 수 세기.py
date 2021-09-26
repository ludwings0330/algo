MOD = 10**4 + 7

n = int(input())
# 점화식 : tiling(n) = tiling(n-1) tiling(n-2)
# dynamic programming

def tiling(width):
    if width <= 1:
        return 1

    if cache[width] != -1:
        return cache[width]

    cache[width] = (tiling(width-2) + tiling(width-1)) % MOD
    return cache[width]

cache = [-1] * (n+1)
print(tiling(n))