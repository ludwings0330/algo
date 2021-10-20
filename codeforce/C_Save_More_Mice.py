import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

def solve():
    ret = 0


    return ret


while T:
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    for i in range(k):
        x[i] = n - x[i]

    x.sort()

    ans = 1
    t = x[0]
    i = 1
    while i < k and t < n:
        t += x[i]
        if t >= n:
            break
        ans += 1
        i += 1

    print(ans)

    T -= 1
'''

고양이 1 마리
쥐 K 마리
고양이의 위치 0
구멍의 위치 n
쥐의 위치 xi

각 pos엔 많은 쥐들이 위치 가능

1초 동안,
1. 한마리 쥐가 오른쪽으로 1 간다
2. 쥐가 구멍에 닿으면 숨는다
3. 쥐가 움직이고 나서 고양이가 1 만큼 움직인다.
4. 고양이 위치에 쥐가 있으면 쥐를 먹는다.

매초마다 움직일 쥐를 선택해서 최대한 많이 살려라.

1 <= test Case <= 10**4
2 <= n <= 10**9
1 <= k <= 4* 10 **5
1 <= xi < n

'''
