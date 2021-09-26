# 부피와 절박도가 있음

C = int(input())

def choice(capacity, item): # 용량이 capacity 만큼 남았을때, item 이후의 물건들을 싸서 얻을 수 있는 절박도
    if item == N: # 더 담을 물건이 없다.
        return 0
    if cache[capacity][item] != -1:
        return cache[capacity][item]

    # 이 물건을 챙기지 않을때
    cache[capacity][item] = choice(capacity, item + 1)
    if capacity >= items[item][1]: # 이 물건을 담을 수 있다면
        # 이 물건을 챙길때
        cache[capacity][item] = max(cache[capacity][item], choice(capacity - items[item][1], item + 1) + items[item][2])

    return cache[capacity][item]
1

def reconstruct(capacity, item, picked):
    if item == N:
        return

    if choice(capacity, item) == choice(capacity, item+1):
        reconstruct(capacity, item+1, picked)
    else:
        picked.append(items[item][0])
        reconstruct(capacity - items[item][1], item+1, picked)


for testCase in range(1, C+1):
    N, W = map(int, input().split())
    # N: 가져가고 싶은 물건의 수, W : 캐리어의 용량
    items = []
    for i in range(N):
        item = input().split()
        item[1] = int(item[1])
        item[2] = int(item[2])
        items.append(item)
        # 이름, 부피, 절박도

    cache = [[-1] * (N+1) for _ in range(W+1)]
    # cache[capacity][item]

    # 가져갈수 있는 물건들의 최대 절박도 합과 가져갈 물건들의 개수를 출력
    # 이후 한줄에 하나씩 각 물건들의 이름을 출력합니다.
    MAX = choice(W, 0)
    pickedItems = []
    reconstruct(W, 0, pickedItems)
    print(MAX, len(pickedItems))
    for item in pickedItems:
        print(item)
