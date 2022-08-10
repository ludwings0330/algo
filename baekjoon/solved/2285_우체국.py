import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
town = []
p_sum = 0
for i in range(N):
    x, a = map(int, input().split())
    p_sum += a
    town.append([x, a])

town.sort()

count = 0
for i in range(N):
    count += town[i][1]
    if count*2 >= p_sum:
        print(town[i][0])
        break

