import sys
input = sys.stdin.readline
MAX = 1000001

N = int(input())
M = int(input())
line = list(map(int, input().split()))
button = [i for i in range(10)]
for b in line:
    button[b] = -1

for i in range(MAX):
    for b in str(i):
        if button[int(b)] == -1:
            break
