C = int(input())
MOD = 10**7
def poly(n, first):
    # n 개중에 첫줄에 first개가 있을때, 만들수 있는 폴리오미노의 수
    if n == first:
        return 1
    if cache[n][first] != -1:
        return cache[n][first]

    cache[n][first] = 0
    ret = 0
    for second in range(1, n-first+1):
        add = second + first - 1
        if first == 0:
            add = 1

        add *= poly(n-first, second)
        add %= MOD
        ret += add
        ret %= MOD

    cache[n][first] = ret
    return ret

for testCase in range(1, C+1):
    n = int(input())
    cache = [[-1] * (n+1) for _ in range(n+1)]

    print(poly(n, 0))
# 첫째 줄에 first 개가 있을때, n개로 폴리오미노를 만드는 방법의 수
# 만약, 첫째 줄에 5개가 있다?
# 그럼 둘째 줄에 있을 수 있는 경우는 poly(n-5, 1) + poly(n-5, 2) + poly(n-5, 3) + poly(n-5, 4) + poly(n-5, 5) ... +poly(n-5, n-5)
# 놓을 수 있는 방법은 첫째줄에 first개 , 둘째줄에 second 개 면 놓을 수 있는 방법의 수는 (fisrt + second -1) 가지의 방법이 있다.
# 완전 탐색에서 시간이 많이 소요되니까 메모제이션을 적용한다.
