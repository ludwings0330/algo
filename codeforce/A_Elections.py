import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
while T:
    a, b, c = map(int, input().split())

    answer = [0, 0, 0]

    MAX = max(a, b, c)

    cnt = 0
    cnt = cnt + 1 if a == MAX else cnt
    cnt = cnt + 1 if b == MAX else cnt
    cnt = cnt + 1 if c == MAX else cnt

    if cnt == 1:
        a = 0 if a == MAX else MAX - a + 1
        b = 0 if b == MAX else MAX - b + 1
        c = 0 if c == MAX else MAX - c + 1
    else:
        a = 1 if a == MAX else MAX - a + 1
        b = 1 if b == MAX else MAX - b + 1
        c = 1 if c == MAX else MAX - c + 1

    answer = [a, b, c]

    print(*answer)

    T -= 1
