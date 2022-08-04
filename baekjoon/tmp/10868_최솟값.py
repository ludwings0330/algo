import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

def init(left, right, idx):
    if left == right:
        segment_tree[idx] = arr[left]
        return

    mid = (left + right) // 2

    init(left, mid, idx * 2)
    init(mid + 1, right, idx * 2 + 1)

    segment_tree[idx] = min(segment_tree[idx*2], segment_tree[idx*2 + 1])


def query(left, right, query_left, query_right, idx):
    if query_right < left or right < query_left:
        return INF
    if query_left <= left and right <= query_right:
        return segment_tree[idx]

    mid = (left + right) // 2
    return min(query(left, mid, query_left, query_right, idx*2), query(mid + 1, right, query_left, query_right, idx*2 + 1))



N, M = map(int, input().split())
arr = [-1]
height = 0

while N > 2**height:
    height += 1

segment_tree = [-1] + [0] * (1 << (height + 1))

for i in range(N):
    arr.append(int(input()))

init(1, N, 1)
for tc in range(M):
    a, b = map(int, input().split())
    print(query(1, N, a, b, 1))