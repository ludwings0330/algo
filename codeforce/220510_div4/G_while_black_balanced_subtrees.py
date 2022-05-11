import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for test_case in range(t):
    n = int(input())
    a = [0, 0] + list(map(int, input().split()))
    s = ['R'] + list(input())

    count = [[0, 0] for i in range(n + 1)]



    answer = 0
    for a, b in count:
        if a == b:
            answer += 1

    print(answer)
