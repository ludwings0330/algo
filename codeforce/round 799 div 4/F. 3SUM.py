import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 10

    for ai in a:
        cnt[ai % 10] += 1

    v = []
    for i in range(10):
        for j in range(0, min(cnt[i], 3)):
            v.append(i)

    m = len(v)
    ans = False

    for i in range(m):
        for j in range(i+1, m):
            for k in range(j+1, m):
                if (v[i] + v[j] + v[k]) % 10 == 3:
                    ans = True
                    break
            if ans:
                break
        if ans:
            break

    print('YES' if ans else 'NO')
