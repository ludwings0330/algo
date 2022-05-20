import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1

    n = int(input())
    candies = list(map(int, input().split()))

    left = weight = result = 0
    count = 0
    right = len(candies) - 1
    while left <= right:
        if weight == 0:
            result = count
            weight += candies[left]
            left += 1
            count += 1
        elif weight < 0:
            weight += candies[left]
            left += 1
            count += 1
        else:
            weight -= candies[right]
            right -= 1
            count += 1
    if weight==0:
        result = count
    print(result)