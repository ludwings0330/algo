import sys
input = lambda:sys.stdin.readline().rstrip()

T = int(input())
cache = [-1] * (10**6 + 1)
cache2= [-1] * (10**6 + 1)
cache[0] = 0
cache[1] = 7
cache[2] = 33
cache2[0]=0
cache2[1] = 3
cache2[2] = 13


DIV = 10**9 + 7

for i in range(2, 10**6+1):
    cache[i] = cache[i-1]*3 + cache2[i-1]*4
    cache2[i] = cache[i-1] + 2 * cache2[i-1]
    cache[i] %= DIV
    cache2[i] %= DIV

while T:
    N = int(input())
    print(cache[N])
    T-= 1
