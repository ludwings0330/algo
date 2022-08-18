p = [1, 1, 2, 2, 2, 8]
i = list(map(int,input().split()))
print(*[p[k] - i[k] for k in range(len(p))])