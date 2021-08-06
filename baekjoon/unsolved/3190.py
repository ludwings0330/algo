import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

MAP = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    MAP[r-1][c-1] = 1 # 사과

MAP[0][0] = 2
L = int(input())

UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

direction = RIGHT
answer = 0

x, y = 0, 0
snake = [[0, 0, RIGHT]]

def move(n, direction):
    global snake, answer
    x = snake[0][0]
    y = snake[0][1]

    for _ in range(n):
        for i in range(len(snake)):
            x = snake[i][0]
            y = snake[i][1]
            d = 
    return True

for _ in range(L):
    X, C = input().split()
    X = int(X)
    if not move(X, direction):
        break

    if C == 'L': # 왼쪽
        if direction == RIGHT:
            direction = UP
        elif direction == LEFT:
            direction = DOWN
        elif direction == UP:
            direction = LEFT
        elif direction == DOWN:
            direction = RIGHT

    elif C == 'D': # 오른쪽
        if direction == RIGHT:
            direction = DOWN
        elif direction == LEFT:
            direction = UP
        elif direction == UP:
            direction = RIGHT
        elif direction == DOWN:
            direction = LEFT

print(answer)