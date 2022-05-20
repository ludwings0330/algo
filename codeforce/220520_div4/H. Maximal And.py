import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ones = defaultdict(int)

    for nums in arr:
        digit = 0
        while nums:
            if nums % 2 == 1:
                ones[digit] += 1
            nums //= 2
            digit += 1

    digits= []
    for digit in range(30, -1, -1):
        if ones[digit] == n:
            digits.append(digit)
        elif n - ones[digit] <= k:
            k -= n - ones[digit]
            digits.append(digit)

    result = 0
    for d in digits:
        result += 2**d
    print(result)