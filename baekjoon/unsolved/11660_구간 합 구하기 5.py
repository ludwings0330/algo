import sys
inp = sys.stdin.readline
if __name__ == "__main__":
    N, M = map(int, input().split())
    numList = [[0]*(N+1)]

    for i in range(N):
        tmpList = [0]
        tmpList.extend(list(map(int, inp().rstrip().split())))

        for j in range(1, len(tmpList)):
            tmpList[j] += tmpList[j-1]

        for j in range(len(tmpList)):
            tmpList[j] += numList[i][j]

        numList.append(tmpList)


    while M:
        M -= 1
        x1, y1, x2, y2 = map(int, inp().split())
        answer = 0
        answer = numList[x2][y2] - numList[x1-1][y2] - numList[x2][y1-1] + numList[x1-1][y1-1]
        print(answer)

# 왤케 틀렸나 했더니 x가 행이고 y 가 열이라서 착각하고 있어서 어디가 틀린지 조차 몰랐음