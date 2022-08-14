import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 10 ** 9
t = int(input())

def init(left, right, idx):
    if left == right:
        segment_tree[idx] = a[left]
        return

    mid = (left+right)//2
    init(left, mid, idx*2)
    init(mid+1, right, idx*2 + 1)
    segment_tree[idx] = min(segment_tree[idx*2], segment_tree[idx*2+1])


def query(left, right, query_left, query_right, idx):
    if query_right < left or right < query_left:
        return MAX
    if query_left <= left and right <= query_right:
        return segment_tree[idx]
    mid = (left + right)//2

    return min(query(left, mid, query_left, query_right, idx * 2),
               query(mid+1, right, query_left, query_right, idx*2 + 1))


while t:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sorted_a = sorted(enumerate(a), key = lambda x:x[1])
    for i in range(k):
        a[sorted_a[i][0]] = MAX
    a = [-1] + a
    height = 0
    while len(a) > (1 << height):
        height += 1
    tree_size = (1 << height+1)
    segment_tree = [0] * tree_size
    init(1, len(a)-1, 1)
    print(segment_tree[1])
