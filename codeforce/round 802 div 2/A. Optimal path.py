import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

while t:
    t -= 1
    n, m = map(int, input().split())

    answer = 0
    for i in range(1, m):
        answer += i
    for i in range(m, n*m+1, m):
        answer += i

    print(answer)
