import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())


def max_init(left, right, idx):
    if left == right:
        max_tree[idx] = arr[left]
        return

    mid = (left + right) // 2

    max_init(left, mid, idx * 2)
    max_init(mid + 1, right, idx * 2 + 1)

    max_tree[idx] = max(max_tree[idx * 2], max_tree[idx * 2 + 1])


def sum_init(left, right, idx):
    if left == right:
        sum_tree[idx] = arr[left]
        return

    mid = (left + right) // 2

    sum_init(left, mid, idx * 2)
    sum_init(mid + 1, right, idx * 2 + 1)

    sum_tree[idx] = sum_tree[idx * 2] + sum_tree[idx * 2 + 1]


while t:
    t -= 1
    n = int(input())
    arr = [-1] + list(map(int, input().split()))
    height = 0
    while n > 2 ** height:
        height += 1

    max_tree = [0] * (1 << (height + 1))
    sum_tree = [0] * (1 << (height + 1))
    max_init(1, n, 1)
    sum_init(1, n, 1)
