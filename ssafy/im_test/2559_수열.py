N, K = map(int, input().split())
temperatures = list(map(int, input().split()))
answer = sum(temperatures[:K])
s, e = 0, K
tmp = answer
while e < N:
    tmp = tmp - temperatures[s] + temperatures[e]
    answer = max(answer, tmp)
    s += 1
    e += 1
print(answer)