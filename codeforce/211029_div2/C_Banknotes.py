'''
n 개 타입의 banknotes

f(s) 최소한의 지폐로 가격 s 를 만들기다.

n, k가 주어질때,
k 개 미만의 지폐로 만들 수 없는 s의 최소 값
1 <= k <= 10**9

k개 미만의 지폐로 만들 수 있는 모든 경우의 수 만들기? 이건 말도 안돼 경우의 수가 너무 많아 심지어 메모리도 감당 못함


4
3 13
0 1 2
2 777
0 4
3 255
0 1 3
10 1000000000
0 1 2 3 4 5 6 7 8 9



59
778
148999
999999920999999999

'''


import sys
input = lambda: sys.stdin.readline().rstrip()


t = int(input())
def solve(n, k, d):
    ret = 0
    for i in range(n-1):
        t = d[i+1]//d[i]
        t -= 1
        if k >= t:
            k -= t
            ret += d[i] * t
            if k == 0:
                ret += d[i+1]
        else:
            ret += d[i] * (k+1)
            k = 0

        if k == 0:
            break

    if k != 0:
        ret += d[-1] * (k + 1)

    return ret

while t:
    t -= 1
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    d.sort()

    for i in range(n):
        d[i] = 10**d[i]

    print(solve(n, k, d))