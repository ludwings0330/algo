import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
words = [input() for _ in range(N)]

info = defaultdict(int)

for word in words:
    for i, ch in enumerate(word):
        info[ch] += 10**(len(word) - i - 1)

trans = {}
num = 9
for key, _ in sorted(info.items(), key=lambda x: -x[1]):
    trans[key] = str(num)
    num -= 1

for i in range(len(words)):
    words[i] = list(words[i])
    for j in range(len(words[i])):
        words[i][j] = trans[words[i][j]]

result = 0
for word in words:
    result += int(''.join(word))

print(result)