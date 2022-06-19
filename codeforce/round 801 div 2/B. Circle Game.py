import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))

    winner = -1
    # mike always win when n is odd
    if n % 2 == 1:
        winner = 0
    else:
        mn = min(a)
        for i in range(n):
            if a[i] == mn:
                if i % 2 == 0:
                    winner = 1
                else:
                    winner = 0
                break

    print("Mike" if winner == 0 else "Joe")