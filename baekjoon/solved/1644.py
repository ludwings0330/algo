import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
if N == 1:
    print(0)
else:
    isMinor = [True] * (N + 1)
    Minor = []
    for n in range(2, N + 1):
        if isMinor[n] == 1:
            Minor.append(n)
        k = 2
        while n * k <= N:
            isMinor[n * k] = 0
            k += 1

    ans = 0
    s = 0
    e = 0
    n = Minor[0]

    while True:
        if n == N:
            ans += 1
            e += 1
            if e >= len(Minor) or s == e:
                break
            n += Minor[e]

        elif n < N:
            e += 1
            if e >= len(Minor):
                break
            else:
                n += Minor[e]

        elif n > N:
            s += 1
            n -= Minor[s - 1]
    print(ans)