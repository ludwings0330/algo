import sys
input = lambda: sys.stdin.readline().rstrip()

test_case = int(input())

for tc in range(test_case):
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]

    answer = float('inf')
    for l in range(n):
        for r in range(l+1, n):
            count = 0
            for i in range(m):
                count += abs(ord(words[l][i]) - ord(words[r][i]))
            answer = min(answer, count)
    print(answer)