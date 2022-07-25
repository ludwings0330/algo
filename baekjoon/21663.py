import sys
sys.setrecursionlimit(10 ** 5)
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

f = list(input())
bool_dict = defaultdict(list)

for i in range(4):
    bool_dict[f[i]].append((i//2, i%2))


def solve(arr, remains):
    if remains == 0:
        return arr

    ret = [-1]
    for a, b in bool_dict[arr[-1]]:
        if b == int(arr[-1]):
            ret = solve(arr + [str(a)], remains-1)
            if ret != [-1]:
                return ret

    return ret


ans = solve(["1"], N-1)
if len(ans) > 1:
    print(''.join(ans[::-1]))
else:
    print('No solution')