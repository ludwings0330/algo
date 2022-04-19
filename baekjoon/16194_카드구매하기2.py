N = int(input())

P = [0] + list(map(int, input().split()))

# 카드 N 개를 갖기 위해 지불해야하는 금액의 최솟값 출력
INF = 10000 * 1000
cache = [INF] * (N+1)
cache[0] = 0
cache[1] = P[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        cache[i] = min(cache[i], cache[i-j] + P[j])

print(cache[N])
