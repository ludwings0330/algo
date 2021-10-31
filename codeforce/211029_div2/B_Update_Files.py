'''
n 컴퓨터에 업데이트
n 개의 컴퓨터
k 개의 케이블
최초 1개의 컴퓨터에 설치
케이블끼리 1:1 연결
1<=t <= 10 **5
1 <= k <= n <= 10**18


4
8 3
6 6
7 1
1 1


4
3
6
0

'''

import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

def pow(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    if k % 2 == 0:
        return pow(n, k//2)**2
    else:
        return pow(n, k-1)* n

cache = [pow(2, i) for i in range(60)]

def solve(n, k):
    ret = 0

    s = 0
    while 2**s <= k:
        ret += 1
        n -= cache[s]
        s += 1

    ret += n//k
    if n % k != 0:
        ret += 1

    return ret

while t:
    t -= 1

    n, k = map(int, input().split())

    print(solve(n-1, k))