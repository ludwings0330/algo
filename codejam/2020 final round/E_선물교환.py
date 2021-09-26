import sys
input = lambda: sys.stdin.readline().rstrip()


TC = int(input())
while TC:
    TC -= 1
    N, M = map(int, input().split())
    # 1 <= N <= 1000
    # 1 <= M <= 100,000

    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    # X[i] 가 Y[i]에게 선물을 주는 경우 0
    # X[i] 가 Y[i]에게 선물을 받는 경우 1

    # 각 임직원 i에 대하여 받는 선물의 수와 주는 선물의 수 차이가 2 미만이어야 한다
