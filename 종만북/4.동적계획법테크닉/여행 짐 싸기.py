# 주어진 용량 내에서 절박도를 최대화
import sys
input = lambda: sys.stdin.readline().rstrip()

# 남은 용량이 capacity 일때 item 이후의 물품을 선택했을때 최대 절박도
def pack(capacity, item):
    if item == n:
        return 0

    if cache[capacity][item] != -1:
        return cache[capacity][item]

    cache[capacity][item] = pack(capacity, item+1)

    if vol[item] <= capacity:
        candidate = des[item] + pack(capacity - vol[item], item + 1)
        if cache[capacity][item] < candidate:
            cache[capacity][item] = candidate
    pack(capacity, item+1)

    return cache[capacity][item]


def reconstruct(capacity, item):
    if item == n:
        return
    if pack(capacity, item) == pack(capacity, item + 1):
        reconstruct(capacity, item+1)
    else:
        picked.append(name[item])
        reconstruct(capacity - vol[item], item + 1)


t = int(input())
while t:
    t -= 1
    n, w = map(int, input().split())
    cache = [[-1] * n for _ in range(w)]
    items = []
    vol = []
    des = []
    picked = []
    for _ in range(n):
        name, v, d = input().split()
        items.append(name)
        vol.append(int(v))
        des.append(int(d))

    pack(w, 0)
    reconstruct(w, 0)
    print(*picked)