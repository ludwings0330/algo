import sys
from collections import  deque
input = sys.stdin.readline


def solve(index, left, right, n):

    if (dq[0][2], dq[-1][2], index) in dp: # 이건 가봤자 실패야
        return False

    # minheap[index]를
    if index == -1:
        if left == 0 or right == 0:
            return False
        else:
            while dq:
                a, aa, n = dq.popleft()
                print(n+1, end= ' ')
            print()
            return True
    # 1. left에 추가
    if minheap[index][0] != dq[0][0]: # 강한 단조 증가의 경우에만 추가, 연속된 숫자는 넣을 수 없음
        if n < 2 or ((minheap[index][1] - dq[0][1]) * (dq[0][1] - dq[1][1])) < 0:
            dq.appendleft(minheap[index])
            if solve(index-1, dq[0][0], right, n+1):
                return True
            dq.popleft()

    # 2. right에 추가
    if dq[-1][0] != minheap[index][0]: # 강한 단조 감소의 경우에만 추가
        if n < 2 or ((dq[n-2][1] - dq[n-1][1]) * (dq[n-1][1] - minheap[index][1])) < 0:
            dq.append(minheap[index])
            if solve(index-1, left, dq[-1][0], n+1):
                return True
            dq.pop()
    dp.add((dq[0][2], dq[-1][2], index))
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
    dp = set()
    dq = deque()
    dq.append(minheap[-1]) # 최대값을 dq 에 넣는다. 이게 k 임
    if not solve(n-2, 0, 0, 1):
        print(-1)