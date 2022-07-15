from collections import defaultdict

arr = list(map(int, input().split()))
store = defaultdict(int)

for num in arr:
    store[num] += 1

for key, item in store.items():
    if item == 1:
        print(key)
        break