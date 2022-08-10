import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
lamps = [list(map(lambda x: False if x == "0" else True, list(input()))) for _ in range(R)]
lamps_toggled = [[False] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        lamps_toggled[r][c] = not lamps[r][c]
K = int(input())


def check():
    cnt = 0

    for r in range(R):
        flag = True
        for c in range(C):
            if toggled[c]:
                if not lamps_toggled[r][c]:
                    flag = False
                    break
            else:
                if not lamps[r][c]:
                    flag = False
                    break
        if flag:
            cnt += 1

    return cnt

# 스위치를 누른다 - 2*n + 1
# 스위치를 누르지 않는다 - 2*n 짝수번 남으면 지금 선택과 동일
ans = 0
toggled = [False] * C
visited = [[False] * C for _ in range(K)]
def solve(c, k):
    if c == C:
        # 홀수번 남으면 다른거 하나를 꺼야한다.
        if k % 2 == 1:
            return

        global ans
        ans = max(ans, check())
        return
    if visited[k][c]:
        return

    visited[k][c] = True
    
    toggled[c] = True
    solve(c+1, k-1)
    toggled[c] = False
    solve(c+1, k)

solve(0, K)
print(ans)