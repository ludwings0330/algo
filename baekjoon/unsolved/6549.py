# Title : 히스토그램에서 가장 큰 직사각형
# Tag : 세그먼트 트리, 분할 정복

import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)


def init(node, start, end):
    if start == end:
        tree[node] = start # idx 저장
        return


    mid = (start + end) // 2
    init(node*2, start, mid)
    init(node*2 + 1, mid+1, end)

    idx_a = tree[node*2]
    idx_b = tree[node*2+1]

    tree[node] = idx_a if line[idx_a] <= line[idx_b] else idx_b

def query(node, start, end, start_query, end_query):
    if start_query <= start and end <= end_query:
        return tree[node]
    if end_query < start or end < start_query:
        return 0

    mid = (start + end) // 2

    idx_a = query(node*2, start, mid, start_query, end_query)
    idx_b = query(node*2 +1, mid +1, end, start_query, end_query)

    return idx_a if line[idx_a] <= line[idx_b] else idx_b

def divide_conquer(left, right):
    min_h_idx = query(1, 1, N, left, right)
    ret = line[min_h_idx] * (right - left + 1)

    mid = (left + right)//2
    if left == right:
        return ret
    if left <= min_h_idx - 1:
        ret = max(ret, divide_conquer(left, min_h_idx - 1))
    if min_h_idx + 1 <= right:
        ret = max(ret, divide_conquer(min_h_idx + 1, right))

    return ret


while True:
    line = list(map(int, input().split()))

    N = line[0]
    if N == 0:
        break
    line[0] = sys.maxsize

    LOG = 18
    tree = [0] * (2 ** LOG)
    init(1, 1, N)
    print(divide_conquer(1, N))
