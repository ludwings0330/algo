import sys
input = lambda: sys.stdin.readline().rstrip()
R, C = map(int, input().split())

origin = [list(input()) for _ in range(R)]
input()
copy = [list(input()) for _ in range(R)]

count = 0
for r in range(R):
    for c in range(C):
        if origin[r][c] == copy[r][c]:
            count += 1

print(count)