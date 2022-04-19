import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# 1 <= N <= 10_000
N = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())


def solution(start, end):
    dq = deque()

    dq.append([start, 0])
    # 현재 위치, 점프횟수

    visit = [False] * (N+1)
    visit[start] = True
    ret = -1

    while dq:
        current, jump = dq.popleft()
        if current == end:
            ret = jump
            break

        k = 1
        n = bridge[current]
        next = current + n * k

        while next <= N:
            if not visit[next]:
                dq.append([next, jump + 1])
                visit[next] = True
            k += 1
            next = current + n * k

        k = 1
        n = bridge[current]
        next = current - n * k
        while next > 0:
            dq.append([next, jump + 1])
            visit[next] = True
            k += 1
            next = current - n * k

    return ret

print(solution(a, b))
