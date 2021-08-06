import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

robots = [False] * (N*2)
s, e = 0, N-1
dq = deque()
ans = 0

def beltRotation():
    global s, e
    s -= 1
    if s == -1:
        s = 2*N-1
    e -= 1
    if e == -1:
        e = 2*N-1

def robotRotation():
    dq.append(-1)

    while dq:
        index = dq.popleft()
        if index == -1:
            break
        if index == e: # 현재 위치가 내리는 위치면 그냥 내려준다.
            robots[e] = False
            continue

        # 현재 위치가 index 인데, index + 1 로 이동 가능한지 확인하고 이동한다.
        next = index + 1 if index+1 != 2*N else 0

        if A[next] > 0 and not robots[next]:
            dq.append(next)
            robots[index] = False #현재 자리를 비우고 이동한다.
            robots[next] = True #
            A[next] -= 1
            if A[next] == 0:
                global ans
                ans += 1
        else: # 이동하지 못하면 그대로 둔다.
            dq.append(index)

def putRobotUp():
    global ans
    if A[s] > 0:
        dq.append(s)
        robots[s] = True
        A[s] -= 1
        if A[s] == 0:
            ans += 1

cnt = 0
while True:
    cnt += 1
    beltRotation()
    robotRotation()
    putRobotUp()

    if ans >= K:
        break
print(cnt)