import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

while t:
    t -= 1
    n = int(input())

    if n == 1:
        print(0)
        continue

    isZero = set()
    arr = list(map(int, input().split()))
    right = n
    arr.reverse()
    cache = -1
    while cache != right:
        cache = right
        for i in range(right):
            # >=
            if arr[i] in isZero:
                isZero.update(arr[i:right])
                right = i
                break

            if i < n-1 and arr[i] < arr[i+1]:
                isZero.update(arr[i+1:right])
                right = i+1
                break



    print(len(isZero))