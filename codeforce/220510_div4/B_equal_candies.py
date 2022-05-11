import sys
inpu = lambda:sys.stdin.readline().rstrip()

tc = int(input())
for test_case in range(tc):
    # number of boxes
    n = int(input())
    candies = list(map(int, input().split()))
    eat = min(candies)

    answer = 0
    for candy in candies:
        answer += candy - eat
    print(answer)


