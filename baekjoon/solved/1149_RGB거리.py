import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
houseList = []
# index : 0 ~ N-1

N = int(input())
for i in range(N):
    houseList.append(list(map(int, input().rstrip().split())))
dpList = [[0]*3 for _ in range(N)]

def dpSolve(k, c):
    if k == N-1:
        return
    elif k == 0:
        dpList[0] = houseList[0]

    for i in range(3): # i 번째 집의 최소값을 선택하는 과정
        for j in range(3):
            if i != j: #서로 다른ㅂ집일때만?
                if dpList[k + 1][i] == 0:
                    dpList[k + 1][i] = dpList[k][j] + houseList[k+1][i]
                else:
                    dpList[k + 1][i] = min(dpList[k + 1][i], dpList[k][j] + houseList[k+1][i])
                # 다음층으로 넘어가야지
    dpSolve(k + 1, c)

    return min(dpList[-1])



print(dpSolve(0, 0))