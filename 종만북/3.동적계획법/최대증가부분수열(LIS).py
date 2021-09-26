C = int(input())
def LIS(start):
    if cache[start + 1] != -1:
        return cache[start + 1]

    cache[start + 1] = 1
    for next in range(start + 1, N):
        if start == -1 or A[start] < A[next]: # 옆에 높이 더 크면 들어간다!
            cache[start + 1] = max(cache[start+1], LIS(next) + 1) # 다음놈이 더 크니까 크기를 1 더해주면서 다음 놈으로 들어갔다.

    return cache[start + 1]


for testCase in range(1, C+1):
    N = int(input())
    A = list(map(int, input().split()))

    cache = [-1] * (N + 1)
    print(LIS(-1) - 1)
