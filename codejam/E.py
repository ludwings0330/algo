import sys
from collections import  deque
input = sys.stdin.readline


def solve(index, left, right, n):
    # minheap[index]를
    if index == -1:
        while dq:
            a, aa, n = dq.popleft()
            print(n+1, end= ' ')
        print()
        return True

    # 1. left에 추가
    fLeft = ((minheap[index][0] != dq[0][0]) and (minheap[index][1] - dq[0][1]) * (dq[0][1] - dq[1][1])) < 0
    fRight = ((dq[-1][0] != minheap[index][0]) and (dq[n-2][1] - dq[n-1][1]) * (dq[n-1][1] - minheap[index][1])) < 0
    if fLeft and fRight:
        if abs(minheap[index][1]-dq[0][1]) > abs(minheap[index][1]-dq[-1][1]):
            fRight = False
        else:
            fLeft = False

    if fLeft:
        dq.appendleft(minheap[index])
        if solve(index-1, left+1, right, n+1):
            return True
        dq.popleft()
    elif fRight:
        dq.append(minheap[index])
        if solve(index - 1, left, right + 1, n + 1):
            return True
        dq.pop()


    return False


T = int(input())
while T:
    T -= 1

    n = int(input().rstrip())
    H = list(map(int, input().rstrip().split()))
    R = list(map(int, input().rstrip().split()))

    minheap = []

    for i in range(n):
        minheap.append([H[i], R[i], i])

    minheap.sort()

    dq = deque()
    dq.append(minheap[n-1]) # 최대값을 dq 에 넣는다. 이게 k 임
    dq.append(minheap[n-2]) # 오른쪽에 -1을 넣는다 방향을 뒤집어도 똑같기때문에 상관 없음
    if not solve(n-3, 0, 1, 2):
        print(-1)