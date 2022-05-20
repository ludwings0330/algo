import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))

    odd = arr[::2]
    even = arr[1::2]

    odd_f = True
    for n in odd:
        if odd[0]%2 != n%2:
            odd_f = False
            break

    even_f = True
    for n in even:
        if even[0]%2 != n%
            even_f = False
            break
    print("YES" if odd_f and even_f else "NO")
