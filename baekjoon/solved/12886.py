import sys
from collections import deque
input = sys.stdin.readline

# rockList = list(map(int, input().split()))
pair = dict()

def BFS():
    dq = deque()
    rockList.sort()
    dq.append(rockList)
    ret = 0

    while dq:
        node = dq.popleft()
        A, B, C = node
        if A == B == C:
            ret = 1
            break

        if A not in pair or C not in pair[A]:
            if A not in pair:
                pair[A] = [C]
            else:
                pair[A].append(C)

            next = sorted([A+A, B-A, C])
            dq.append(next)
            next = sorted([A+A, B, C-A])
            dq.append(next)
            next = sorted([A, B+B, C-B])
            dq.append(next)
    return ret
def BFS2():
    dq = deque()
    rockList.sort()
    dq.append(rockList)
    ret = 0

    while dq:
        node = dq.popleft()
        A, B, C = node
        if A == B == C:
            ret = 1
            break

        if A not in pair or C not in pair[A]:
            if A not in pair:
                pair[A] = [C]
            else:
                pair[A].append(C)

            next = sorted([A+A, B, C-A])
            dq.append(next)
    return ret

for i in range(1, 501):
    for j in range(1, 501):
        for k in range(1, 501):
            rockList = [i, j, k]
            if sum(rockList)%3 != 0:
                # print(0)
                continue

            else:
                pair = dict()
                ret1 = BFS()
                pair = dict()
                ret2 = BFS2()

                if ret1 != ret2:
                    print(i, j, k)
    print(i)