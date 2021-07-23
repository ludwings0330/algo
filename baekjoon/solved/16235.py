import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Nutrients = [[5]*N for _ in range(N)]

trees_dict = {(i, j):deque() for i in range(N) for j in range(N)}

dd = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
for _ in range(M):
    r, c, z = map(int, input().split())
    trees_dict[(r-1, c-1)].append(z)


while K:
    K -= 1
    deadTrees = deque()
    # 봄
    # 양분을 먹을 수 없으면 죽음,
    # 먹을 수 있으면 먹음.
    for (r, c), trees in trees_dict.items():
        newTrees = deque()
        for tree in trees:
            if Nutrients[r][c] >= tree: # 먹을 수 있으면
                Nutrients[r][c] -= tree
                newTrees.append(tree+1)
            else:
                deadTrees.append([r, c, tree//2])
        trees_dict[(r, c)] = newTrees


    #여름
    while deadTrees:
        r, c, z = deadTrees.pop()
        Nutrients[r][c] += z

    #가을
    for (r, c), trees in trees_dict.items():
        Nutrients[r][c] += A[r][c]

        for tree in trees:
            if tree%5 == 0: # 5의 배수이면
                 for i in range(8):
                    dr = r + dd[i][0]
                    dc = c + dd[i][1]
                    if 0 <= dr < N and 0 <= dc < N:
                        trees_dict[(dr, dc)].appendleft(1)


ans = 0
for trees in trees_dict:
    ans += len(trees_dict[trees])

print(ans)