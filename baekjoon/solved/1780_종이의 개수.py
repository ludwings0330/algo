import sys

answer = {-1:0, 0:0, 1:0}

def check(N, leftTop, rightBottom):
    flag = paper[leftTop[1]][leftTop[0]]

    for i in range(leftTop[1], rightBottom[1]):
        for j in range(leftTop[0], rightBottom[0]):
            if paper[i][j] != flag:
                return False

    return True

def NumOfPaper(N, leftTop, rightBottom):
    if check(N, leftTop, rightBottom):
        answer[paper[leftTop[1]][leftTop[0]]] += 1
    else:
        p = N//3
        for i in range(3):
            for j in range(3):
                NewLeftTop = [leftTop[0] + p*j, leftTop[1] + p*i]
                NewRightBottom = [rightBottom[0] - p*(2-j), rightBottom[1] - p*(2-i)]
                NumOfPaper(N//3, NewLeftTop, NewRightBottom)

N = int(input())
# N * N 행렬
paper = []

for i in range(N):
    tmpList = list(map(int, sys.stdin.readline().rstrip().split()))
    paper.append(tmpList)

NumOfPaper(N, [0, 0], [N, N])
print(answer[-1], answer[0], answer[1], sep='\n')