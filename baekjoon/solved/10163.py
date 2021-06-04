import sys
input = sys.stdin.readline

N = int(input())
MAP = [[0]*101 for _ in range(101)]
paper = []
for _ in range(N):
    x, y, w, h = map(int, input().split())
    paper.append([x, y, w, h])

    for i in range(y, y+h):
        for j in range(x, x+w):
            MAP[i][j] = str(_+1)

for _ in range(N):
    x, y, w, h = paper[_]
    answer = 0
    for i in range(y, y+h):
        for j in range(x, x+w):
            if MAP[i][j] == str(_+1):
                answer += 1
    print(answer)