import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = 0
visit = [False] * N
arr = list(map(int, input().split()))

def recursiveSolve(toPick, pre, cnt):
    if toPick == 0:
        global ans
        ans = max(ans, cnt)

        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            if pre != -1:
                recursiveSolve(toPick - 1, i, cnt + abs(arr[pre] - arr[i]))
            else:
                recursiveSolve(toPick - 1, i, 0)
            visit[i] = False

recursiveSolve(N, -1, 0)
print(ans)