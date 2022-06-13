import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, m, k = map(int, input().split())
    a = list(input())
    b = list(input())

    a.sort()
    b.sort()

    idx_a = 0
    idx_b = 0
    c = []

    current = ''
    count_a = 0
    count_b = 0

    while idx_a < n and idx_b < m:
        if a[idx_a] < b[idx_b]:
            current = 'a'
            count_a += 1
            count_b = 0
        else:
            current = 'b'
            count_b += 1
            count_a = 0
        if count_a > k:
            current = 'b'
            count_b = 1
            count_a = 0
        elif count_b > k:
            current = 'a'
            count_a = 1
            count_b = 0

        if current == 'a':
            c.append(a[idx_a])
            idx_a += 1
        else:
            c.append(b[idx_b])
            idx_b += 1

    print(''.join(c))
