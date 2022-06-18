import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

t = int(input())
while t:
    t -= 1
    store = defaultdict(list)
    n = int(input())
    x = list(map(int, input().split()))

    for i in range(n):
        store[x[i]].append(i)

    global_mx = -1
    global_l = -1
    global_r = -1
    ans = -1
    for key in store.keys():
        mx = 0
        for i in range(len(store[key])):
            if mx == 0:
                mx = 1
                l = store[key][i]
                r = store[key][i]
            else:
                mx += 1
                mx -= store[key][i] - store[key][i-1] - 1

                if mx > 1:
                    r = store[key][i]
                else:
                    mx = 1
                    l = store[key][i]
                    r = store[key][i]

            if mx > global_mx:
                global_mx = mx
                global_l = l
                global_r = r

    print(x[global_l], global_l+1, global_r+1)
