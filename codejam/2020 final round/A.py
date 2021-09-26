# title : 장난감 경구
import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

while TC:
    TC -= 1
    N, X, Y = map(int, input().split())
    # 경주 거리 X, 부스터 한계치 Y
    # Z 의 속도로 1 초간 달린다.

    V = [0] + list(map(int, input().split()))
    # 나는 N번 참가자
    T = sys.maxsize
    for i in range(1, N):
        T = min(T, X / V[i])
    Z = int(X - V[N]*(T-1)+1)

    if T > X/V[N]:
        print(0)
    elif Z > Y:
        print(-1)
    else:
        print(Z)