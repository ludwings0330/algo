N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    if graph[r][0] == 1:
        print(f'boss:{r}')
print('under:', end='')
for c in range(N):
    if graph[0][c] == 1:
        print(c, end= ' ')