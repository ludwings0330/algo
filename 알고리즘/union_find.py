import sys
input = lambda:sys.stdin.readline().rstrip()

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x]) # 나의 부모의 부모라도 찾아줘.. 마지막엔 나의 맨 위 부모의 부모는 자기 자신이니까 그정도는 알 수 있잖아
        parent[x] = y
        return y

def union(x, y):
    x = find(x) # x 부모 찾기
    y = find(y) # y 부모 찾기

    if x == y:
        return -1 # 이미 같은 부모라서 합칠 필요가 없다
    # x, y  부모가 다를때,
    #rank 이용 작은 트리가 큰 트리에 붙는다
    if rank[x] > rank[y]: # x가 자식이 더 많을때,
        parent[y] = x # y의 부모를 x로 바꿔준다.
        rank[x] += rank[y] # y가 x의 자식이 되었으니, rank[y]를 더해준다
    else:
        parent[x] = y
        rank[y] += rank[x]
    return 1



if __name__ == "__main__":
    n, m = map(int, input().split())

    parent = [i for i in range(n+1)]
    rank = [1 for i in range(n+1)]

    for _ in range(m):
        c, a, b = map(int, input().split())

        if c == 0:
            union(a, b)
        elif c == 1:
            if find(a) == find(b):
                print('YES')
            else:
                print('NO')