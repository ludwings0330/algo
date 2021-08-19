# segment Tree
import sys
input = lambda: sys.stdin.readline().rstrip()

def init(node, start, end):
    if start == end:
        segment_tree[node] = nums[start]
        return
    mid = (start + end)//2

    init(node*2, start, mid)
    init(node*2 +1 , mid + 1, end)

    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2 + 1]

def update(node, start, end, target, diff):
    if start <= target <= end:
        mid = (start + end)//2
        segment_tree[node] += diff

        if start == end:
            nums[target] += diff
        if start != end:
            update(node*2, start, mid, target, diff)
            update(node*2 + 1, mid +1 , end, target, diff)

def query(node, start, end, query_start, query_end):
    if query_end < start or end < query_start:
        return 0

    if query_start <= start and end <= query_end:
        return segment_tree[node]

    mid = (start + end)//2
    return query(node*2, start, mid, query_start, query_end) + query(node*2 + 1, mid + 1, end, query_start, query_end)

N, Q = map(int, input().split())

nums = [-1] + list(map(int, input().split())) # 초기 수 배열
MAX_SIZE = 2**20
segment_tree = [0] * (MAX_SIZE*2) # 1 <= N <= 100,000 이므로 *2 정도 여유를 줘야 idx error 안난다

init(1, 1, N)
while Q:
    Q -= 1

    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(query(1, 1, N, x, y))
    update(1, 1, N, a, b - nums[a])