import sys
sys.setrecursionlimit(1000000)
A,B,C = map(int, input().split())

def power(n, k):
    if k == 0:
        return 1
    result = power(n, k//2)
    result = (result*result) % C

    if(k%2) == 1:
        result = (result * n) % C
    return result

print(power(A,B))