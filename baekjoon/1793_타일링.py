cache = [-1] * (251)
N = 0

def tiling(n):
    if n < 0: # 남은 타일의 갯수가 없으면 0 이죠
        return 0
    elif n == 0 or n == 1: # 남은 타일의 갯수가 1이면 1x2로 1개만 넣음
        return 1
    elif n == 2: # 남은 갯수가 2이면 3가지 방법으로 넣을 수 있음
        return 3

    if cache[n] != -1:
        return cache[n]

    cache[n] = 0
    cache[n] = tiling(n-1) + 2 * tiling(n-2)

    return cache[n]



def solve():
    global N, cache
    N = int(input())

    return tiling(N)

while True:
    try:
        print(solve())
    except:
        break