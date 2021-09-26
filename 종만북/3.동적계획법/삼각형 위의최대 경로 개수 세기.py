countCache = [[-1] * 100 for _ in range(N)]

N = int(input())
triangle = []

def path(r, c):
    if r == n-1:
        return triangle[r][c]
    if cache[r][c] != -1:
        return cache[r][c]

    ret = max(path(r+1, c), path(r+1, c+1)) + triangle[r][c]
    cache[r][c] = ret
    return ret

n = int(input())
cache = [[-1] * 100 for _ in range(100)]
print(path(0, 0))
# 일반화 count(r, c) : r, c 에서 시작해 맥 아래줄까지 내려가는 최대 경로의 수
# 점화식 count(r, c) = max count(y+1, x)       path(y+1, x) > path(y+1, x+1)
#                         count(y+1, x+1)    path(y+1, x) < path(y+1, x+1)
#                         count(y+1, x) + count(y+1, x+1) path(y+1, x) == path(y+1, x+1)
def count(r, c):
    if r == N-1:
        return 1

    if countCache[r][c] != -1:
        return countCache[r][c]

    countCache[r][c] = 0
    if path(r+1, c+1) >= path(r+1, c) : countCache[r][c] += count(r+1, c+1)
    if path(r+1, c+1) <= path(r+1, c) : countCache[r][c] += count(r+1, c)
    return countCache[r][c]
