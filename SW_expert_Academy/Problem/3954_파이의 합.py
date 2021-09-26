mino = [1 for i in range(1000002)]

for i in range(2, 1000001):
    k = 2
    if mino[i] != 0:
        while i * k < 1000001:
            mino[i*k] = 0
            k += 1

def pi(n):
    if cache[n] != -1:
        return cache[n]

    if mino[n] == 1: # 이미 소수라서 더이상 나눌 수 없다면
        cache[n] = 1 - 1/n
        return cache[n]


    ret = 1
    next = n
    while next != 1:
        for d in range(2, next+1):
            if mino[d] != 1:
                continue

            if next % d == 0:
                ret *= pi(d)

                while next % d == 0:
                    next //= d

                break
    cache[n] = ret
    return ret


def solve(a, b):
    ret = 0
    for i in range(b, a-1, -1):
        ret += i*pi(i)

    return ret

TC = int(input())

cache = [-1] * (1000001)
cache[1] = 1
for testCase in range(1, TC+1):
    a, b = map(int, input().split())
    print("#%d %d" %(testCase, solve(a, b)))

