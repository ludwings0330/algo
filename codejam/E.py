import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
T = int(input())

def recursive_solve(idx):
    if idx == 0:
        dq.append(logs[idx])
        dq.append(logs[idx+1])
        return recursive_solve(idx + 2)

    if idx >= n:
        if dq[-1] == logs[0] or dq[0] == logs[0]:
            return False
        else:
            for (h, r, i) in dq:
                print(i+1, end=' ')
            return True

    ret = False

    left = dq[0][2]
    right = dq[-1][2]
    # add to left
    if (logs[idx][1] - dq[0][1]) * (dq[0][1] - dq[1][1]) < 0:
        dq.appendleft(logs[idx])
        if dp[idx][left][right]:
            ret = recursive_solve(idx + 1)
        dq.popleft()
    if ret:
        return True
    # add to right
    if (dq[-2][1] - dq[-1][1]) * (dq[-1][1] - logs[idx][1]) < 0:
        dq.append(logs[idx])
        if dp[idx][left][right]:
            ret = recursive_solve(idx + 1)
        dq.pop()

    dp[idx][left][right] = False
    return ret

while T:
    T -= 1
    n = int(input())
    logs_h = list(map(int, input().split()))
    logs_r = list(map(int, input().split()))
    logs_idx = [i for i in range(n)]
    logs = list(zip(logs_h, logs_r, logs_idx))
    logs.sort(reverse = True)

    dq = deque()
    dp = [[[True]*(n+1) for _ in range(n+1)] for _ in range(n+1)]

    if not (recursive_solve(0)):
        print(-1)
    else:
        print()