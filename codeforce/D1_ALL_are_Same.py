'''
array of n ( n is even )
integers a1 ,,,,, an
1 <= t <= 10
4 <= n <= 40
-10**6 <= a <= 10**6

'''

import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
while T:
    n = int(input())
    a = list(map(int, input().split()))

    a = list(set(a))
    MIN = min(a)

    ret= 987654321
    for k in a:
        ret = min(ret, MIN - k) if MIN - k != 0 else:


    T -= 1