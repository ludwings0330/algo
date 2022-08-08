import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
pos = sorted([int(input()) for _ in range(N)])
max_gap = pos[-1] - pos[0]

def solve(s, e):
    mid = (s + e) // 2 # 아마 정답은 mid 일 것이다
    if s > e:
        return mid

    idx = 0
    cnt = 1 # 0번째 position 은 이미 선택된 상태
    for i in range(1, N):
        if pos[i] - pos[idx] >= mid: # mid 보다 같거나 크다는 것은 선택 가능하다는 것
            cnt += 1 # 선택 갯수를 센다
            idx = i

    if cnt < C: # 선택할 수 있는 갯수가 선택해야하는 갯수가 적다 -> 더 잘게 쪼개야 정답이 있다
        return solve(s, mid-1)
    else: # 정답이 있을 수 있다 -> 더 크게 쪼갤 수 있다. -> 더 크게 쪼개보자
        return solve(mid+1, e)


print(solve(1, max_gap)) # 답은 1, max_gap 사이에 있다 이진탐색으로 찾자
