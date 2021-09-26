n = int(input())
import sys
sys.setrecursionlimit(10**9)
def change(price, cnt): # 남은 금액 n 이고, 지금까지 사용한 동전이 cnt개 일때 모두 거슬러줬을때 동전의 갯수 change(n, cnt)
    if price == 0:
        return cnt # 몇개의 동전을 사용했는지 비교

    if cache[price] != -1:
        return cache[price]

    cache[price] = 10**9
    if price - 5 >= 0:
        cache[price] = min(cache[price], change(price - 5, cnt + 1))
    if price - 2 >= 0:
        cache[price] = min(cache[price], change(price - 2, cnt + 1)) # 현재 단계에서 알 수 있는건 2원동전을 쓰거나 3원동전을 쓰는것
    

    return cache[price]


# 거스름 동전의 최소 갯수 구하려면?
cache = [-1] * (n+1)
ans = change(n, 0)
print(ans if ans != 10**9 else -1)
