import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
q = int(input())
total = sum(arr)

idx = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 2:
        idx = (idx - query[1] + N) % N
        # rotate
    elif query[0] == 1:
        total -= arr[(idx + query[1] -1 + N) % N]
        total += query[2]
        arr[(idx + query[1] -1 +N) % N] = query[2]

    print(total)