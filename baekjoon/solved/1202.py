# 보석도둑
# 무게 정렬을 한뒤에 가치로 정렬해주는 것을
# 이중 우선순위 큐로 해결
# 무게 정렬을 통해서 가장 가벼운 보석부터 꺼내서 가치로 정렬하는 애를 최대힙에 넣어줘
# 그러다가 들어있는게 가방에 안들어간다.
# 그러면 가치가 가장큰 놈을 뽑아서 넣어준다. 이건 가벼운놈도 아직 그 가치를 가지고 유지하고 있기 떄문에
# 무게가 무거운 놈들로 채워지더라도 가장 높은 가치를 가진 것을 현재 탐색중인 가방에 넣을 수 있는 거야.
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
C = [] # 가방에 넣을 수 있는 최대 무게
jewels = []
for i in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewels, [m, v]) #
for i in range(K):
    C.append(int(input()))
C.sort()

ans = 0
tmpJewels = []
for limit in (C): # 300,000
    while jewels and limit >= jewels[0][0]:
        heapq.heappush(tmpJewels, -heapq.heappop(jewels)[1])
    if tmpJewels: # tmp 보석이 들어있다면 전부다 안들어갈수 있으니까 필요하지
        ans -= heapq.heappop(tmpJewels)
    elif not jewels: # 남은 보석이 없으면 가방이 비어 있을 수도 있으니까
        break
print(ans)