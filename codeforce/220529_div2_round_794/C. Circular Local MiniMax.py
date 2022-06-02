import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    if n % 2 == 1:
        print('NO')
        continue
    m = n // 2
    flag = True
    for i in range(1, m):
        if a[i] == a[i + m - 1]:
            flag = False
            break
    if not flag:
        print('NO')
        continue
    slow, fast = 0, m
    answer = []
    for _ in range(m):
        answer.append(a[slow])
        answer.append(a[fast])
        slow, fast = slow + 1, fast + 1


    print('YES')
    print(*answer)
