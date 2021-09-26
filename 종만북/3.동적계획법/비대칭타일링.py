C = int(input())
MOD = 10**9 + 7
def asymmetric(width):
    if width % 2 == 1: # 홀수면 가운데는 1자
        return (tiling(width) - tiling((width-2)//2) + MOD)% MOD

    else:
        ret = tiling(width)
        ret = (ret - tiling(width//2) + MOD) % MOD
        ret = (ret - tiling((width-2)//2) + MOD) % MOD
    return ret

def tiling(width):
    if width <= 1:
        return 1
    if cache[width] != -1:
        return cache[width]

    cache[width] = (tiling(width - 1) + tiling(width - 2)) % MOD
    return cache[width]


for testCase in range(1, C+1):
    n = int(input())
    cache = [-1] * (n+1)

    print(asymmetric(n))