import sys
input = sys.stdin.readline

N = int(input())
student = {}
board = [[0]*N for _ in range(N)]
studentPos = {n:tuple() for n in range(1, N*N+1)}
for i in range(N):
    for j in range(N):
        c = 4
        if i == 0 or i == N-1 or j == 0 or j == N-1:
            c = 3
            if (i == 0 and j == 0) or (i == N-1 and j == N-1) or \
                    (i == 0 and j == N-1) or (i == N-1 and j == 0):
                c = 2
        board[i][j] = c


for _ in range(N**2):
    c = list(map(int, input().rstrip().split()))
    student[c[0]] = c[1:]

dd = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for n, friends in student: # n 학생번호 , freinds 좋아하는 친구들
    for friend in friends: # friend 좋아하는 친구
        POS = studentPos[friend] # 좋아하는 친구 위치
        if POS: # 위치가 배정되었다면
            x = POS[0]
            y = POS[1]
            for i in range(4):
                dx = x + dd[i]
                dy = y + dd[i]
                if 0 <= dx < N and 0 <= dy < N:
