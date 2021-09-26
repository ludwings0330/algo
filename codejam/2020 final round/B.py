# Tag : 다도해
import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

def find(x):
    if parent[x] == x:
        return x
    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False # 부모가 같으면 다리를 이을 필요가 없음 ㅋ

    if rank[x] > rank[y]: # 더 큰 트리에 작은 놈을 붙인다
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]

    return True


while TC:
    TC -= 1
    N, Seed, A, B = map(int, input().split())

    parent = [i for i in range(N + 1)]
    rank = [1 for i in range(N + 1)]

    visit = set()
    E = Seed % (N**2)

    cnt = 0
    day = 0
    while E not in visit:
        day += 1
        X = E // N
        Y = E % N

        if union(X, Y):
            cnt += 1
        if cnt == N-1:
            print(day)
            break

        visit.add(E)
        E = (E * A + B) % (N**2)
    else:
        print(0)