def dfs_init(current, depth):
    depths[current] = depth

    if current in graph:
        for next in graph[current]:
            if parents[next] == -1:
                parents[next] = current
                dfs_init(next, depth + 1)
                rank[current] += rank[next]

def LCA(node_a, node_b):
    while depths[node_a] != depths[node_b]:
        if depths[node_a] > depths[node_b]:
            node_a = parents[node_a]
        else:
            node_b = parents[node_b]

    while node_a != node_b:
        node_a = parents[node_a]
        node_b = parents[node_b]

    return node_a # 부모의 idx를 보낸다.

TC = int(input())

for i in range(1, TC+1):
    print("#{}".format(i), end = ' ')
    V, E, a, b = map(int, input().split())
    graph ={}
    input_list = list(map(int, input().split()))

    for i in range(E):
        s = input_list[i*2]
        e = input_list[i*2 + 1]

        if s in graph:
            graph[s][e] = 1
        else:
            graph[s] = {e:1}
        if e in graph:
            graph[e][s] = 1
        else:
            graph[e] = {s:1}

    depths = [-1] * (V + 1)
    parents = [-1] * (V + 1)
    parents[1] = 1
    rank = [1] * (V + 1)

    dfs_init(1, 1)
    root = LCA(a, b)
    print(root, rank[root])

    print()