import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)
t = int(input())


def solve(current, length):
    if current == n:
        return length

    ret = length
    for idx in range(current+1, n):
        if arr[idx] > arr[current]:
            ret = max(ret, solve(idx, length + 1))
    return ret


def LIS(start):
    if cache[start+1] != -1:
        return cache[start+1]

    cache[start+1] = 1
    for next in range(start+1, n):
        if start == -1 or arr[start] < arr[next]:
            cache[start+1] = max(cache[start+1], LIS(next) + 1)

    return cache[start+1]


while t:
    t -= 1
    n = int(input())

    arr = list(map(int, input().split()))
    cache = [-1] * 101
    print(LIS(-1)-1)
