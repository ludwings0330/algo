# 상대 두개 빌리자
# 두개의 높이 차이는 H[i] - H[j] <= X
# 두 상자의 부피의 합이 최대가 되는 한 쌍의 상자 고르기
import sys

input = sys.stdin.readline
import heapq

T = int(input())

while T:
    T -= 1
    n, X = map(int, input().rstrip().split())
    hs, ha, hb, hc = map(int, input().rstrip().split())
    ws, wa, wb, wc = map(int, input().rstrip().split())

    H, W = [0 for i in range(n)], [0 for i in range(n)]

    H[0] = hs % hc + 1
    W[0] = ws % wc + 1
    for i in range(1, n):
        H[i] = H[i - 1] + 1 + (H[i - 1] * ha + hb) % hc
        W[i] = (W[i - 1] * wa + wb) % wc + 1

    dp = [0] * n
    s, e = 0, 0
    rank = [[H[0]*W[0], 0], [H[1]*W[1], 1]]
    ans = -1
    for i in range(1, n):
        if rank[0][0] < rank[1][0]:
            rank[0], rank[1] = rank[1], rank[0]
        e = i
        if H[i] - H[s] > X:
            while H[i] - H[s] > X:
                s += 1
                if s == e:
                    break
        if H[i]*W[i] > rank[1][0] and i != rank[0][1]:
            rank[1] = [H[i]*W[i], i]
        if s > rank[1][1] or rank[1][1] > e:
            rank[1] = [-1, -1]
            for j in range(s, e+1):
                if rank[1][0] <= H[j]*W[j] and j != rank[0][1]:
                    rank[1][0] = H[j]*W[j]
                    rank[1][1] = j

        if s > rank[0][1] or rank[0][1] > e:
            rank[0] = [-1, -1]
            for j in range(s, e+1):
                if rank[0][0] <= H[j]*W[j] and j != rank[1][1]:
                    rank[0][0] = H[j]*W[j]
                    rank[0][1] = j

        if rank[0][1] != -1 and rank[1][1] != -1:
            ans = max(ans, rank[0][0] + rank[1][0])
    print(ans)