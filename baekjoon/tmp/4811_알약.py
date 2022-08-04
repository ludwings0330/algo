import sys
input = lambda: sys.stdin.readline().rstrip()


# solve(w, h) 는 약통에 한개짜리 w개, 반개짜리 h개 있을때 만들 수 있는 문자열의 수.
def solve(w, h):
    if w == 0 and h == 0:
        return 1

    if cache[w][h] != -1:
        return cache[w][h]

    cache[w][h] = 0

    # 한개짜리 꺼냈을 때,
    if w > 0:
        cache[w][h] += solve(w-1, h+1)
    # 두개짜리 꺼냈을 때,
    if h > 0:
        cache[w][h] += solve(w, h-1)

    return cache[w][h]


while True:
    N = int(input())
    if N == 0:
        break
    cache = [[-1] * (N+1) for _ in range(N+1)]

    print(solve(N, 0))
