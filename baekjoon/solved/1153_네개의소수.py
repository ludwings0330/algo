import sys
sys.setrecursionlimit(10**5)
prime = []
tmp = [1] * (1_000_000 + 1)
for i in range(2, len(tmp)):
    if tmp[i] == 0:
        continue
    prime.append(i)
    k = 2
    while k * i <= 1_000_000:
        tmp[k*i] = 0
        k += 1

N = int(input())

path = [0] * 4
def solve(n, cnt):
    if n < 0:
        return False
    if cnt == 4:
        if n != 0:
            return False
        print(*path)
        return True

    for p_number in prime:
        if p_number > n:
            break
        path[cnt] = p_number
        if solve(n-p_number, cnt + 1):
            return True
    return False
if not solve(N, 0):
    print(-1)