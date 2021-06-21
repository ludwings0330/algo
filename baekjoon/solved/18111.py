# 마인크래프트
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
# 땅 파는거 2초, 채우는거 1초
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

# Hint 브루트포스
def allLayersToN(n, B):
    time = 0
    localB = B
    for i in range(N):
        for j in range(M):
            if MAP[i][j] > n:
                block = MAP[i][j]-n
                time += block*2
                localB += block
            elif MAP[i][j] < n:
                block = n - MAP[i][j]
                time += block
                localB -= block
            elif MAP[i][j] == 0:
                pass
    if localB < 0:
        return -1
    else:
        return time

MIN = sys.maxsize
f = 0
for n in range(257):
    time = allLayersToN(n, B)

    if time != -1 and MIN >= time:
        MIN = time
        f = n


print(MIN, f, sep=' ')