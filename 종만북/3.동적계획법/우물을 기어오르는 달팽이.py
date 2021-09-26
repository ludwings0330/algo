import sys
input = lambda: sys.stdin.readline().rstrip()

# 깊이가 n 미터인 우물의 맨 밑바닥에 달팽이가 있다.
# 만약 비가 내리면 달팽이는 하루에 2미터를 기어올라 갈 수 있지만
# 날이 맑으면 1 미터밖에 올라가지 못합니다.
# 앞으로 m 일간 각 날짜에 비가 올 확률이 정확히 50% 라고 가정할때, m일 안에 달팽이가 우물 끝까지 올라갈 확률은 얼마나 될까요?
n, m = map(int, input().split())
# n : 깊이가 n 미터인 우물
# m : m 일동안 맨 위로 올라갈 수 있을까?
MAX_N = n +1
MAX_M = m +1

cache = [[-1] * (MAX_N*2) for _ in range(MAX_N)]

def climb(days, height):
    if days == m:
        return 1 if height >= n else 0

    # 메모제이션
    if cache[days][height] != -1:
        return cache[days][height]

    cache[days][height] = climb(days+1, height+1) + climb(days+1, height+2)
    # 만약 비가 올 확률이 50% 가 아니라 75%가 되었을때,
    # 부분 문제의 구조는 유지할수 있다.
    # climb(days, height) = 0.25 * climb(days+1, height+1) + 0.75 * climb(days+1, height+2)
    return cache[days][height]

print(climb(0, 0))
