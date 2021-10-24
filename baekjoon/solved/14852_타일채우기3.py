import sys
sys.setrecursionlimit(10**9)

N = int(input())
DIV = 10**9 + 7

'''
tiling(N) 남은 타일 갯수가 N개 일때, 타일링 방법의수 return
N-1 -> 2x1, 1x1 * 2
N-2 -> 1x2 + 1x1 * 2, 2x1 *2, 1x1 *2 + 1x2
'''
def tiling(n):
    if cache[n] != -1:
        return cache[n]

    cache[n] = tiling(n - 1) * 2 + tiling(n - 2) * 3
    cache[n] %= DIV

    return cache[n]



cache = [-1] * (N+5)
cache[0] = 1
cache[1] = 2
cache[2] = 7
cache[3] = 22



print(tiling(N))