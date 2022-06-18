import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    # dist = list(map(int, input().split()))
    # timur = dist[0]
    # dist.sort(reverse= True)
    # for rank in range(4):
    #     if dist[rank] == timur:
    #         print(rank)
    #         break
    a, b, c, d = map(int, input().split())
    ans = (b > a) + (c > a) + (d > a)
    print(ans)
