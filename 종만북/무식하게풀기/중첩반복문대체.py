
# 3중 포문
n = 7
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            print(i, j, k)


def print_picked(nums: list):
    print(*nums)


def recursive_pick(to_pick: int, picked: list, end: int):
    if to_pick == 0:
        print_picked(picked)
        return

    start = 0 if not picked else picked[-1] + 1
    for n in range(start, end):
        recursive_pick(to_pick - 1, picked + [n], end)
print("recursive_pick  ")
recursive_pick(3, [], n)