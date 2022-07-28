graph = [[0] * 5 for _ in range(5)]

graph[0][2] = graph[1][2] = graph[2][3] = graph[3][4] = 1
name = ["Diane", "Chloe", "Bob", "Amy", "Edger"]

MAX =0
idx = 0
for fr in range(5):
    tmp = 0
    for to in range(5):
        tmp += graph[to][fr]
    if tmp > MAX:
        MAX = tmp
        idx = fr
print(name[idx])