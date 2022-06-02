import sys
input = lambda: sys.stdin.readline()

t = int(input())

while t:
    t -= 1

    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for num in a:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print(min(odd, even))

