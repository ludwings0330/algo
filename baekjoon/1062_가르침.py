import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
words = []
for _ in range(N):
    words.append(set(list(input())))

chars = dict()
idx = list("abcdefghijklnmopqrstuvwxyz")

for ch in list("abcdefghijklnmopqrstuvwxyz"):
    chars[ch] = 0


def count_word():
    ret = len(words)
    for word in words:
        for ch in chars:
            if chars[ch] == 1 and ch not in word:
                ret -= 1
                break
    return ret

def solve(i, remains):
    if remains == 0:
        cnt = count_word()
        return cnt

    ret = 0
    for next in range(i, len(chars)):
        chars[idx[next]] = 1
        ret = max(ret, solve(i+1, remains - 1))
        chars[idx[next]] = 0

    return ret


print(solve(0, K))


