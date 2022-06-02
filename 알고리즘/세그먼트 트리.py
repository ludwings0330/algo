import sys
input = lambda: sys.stdin.readline()

arr = [-1] + [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
height = 0

while len(arr) > 2 ** height:
    height += 1

tree_size = (1 << (height + 1))
segment_tree = [0] * tree_size
print(tree_size)


def init(left, right, idx):
    if left == right:
        segment_tree[idx] = arr[left]
        return

    mid = (left + right) // 2

    init(left, mid, idx * 2)
    init(mid + 1, right, idx * 2 + 1)

    segment_tree[idx] = segment_tree[idx*2] + segment_tree[idx*2+1]


def query(left, right, query_left, query_right, idx):
    # 범위 밖에 있는 경우
    if query_right < left or right < query_left:
        return 0
    # 범위 안에 있는 경우
    if query_left <= left and right <= query_right:
        return segment_tree[idx]
    # 걸쳐 있는 경우 처리 (밖에있거나 안에 있을 때 까지 범위를 쪼갠다.)
    mid = (left + right) // 2
    return query(left, mid, query_left, query_right, idx*2) + query(mid + 1, right, query_left, query_right, idx*2+1)


def update(left, right, target, idx, diff):
    if left <= target <= right:
        mid = (left + right) // 2
        segment_tree[idx] += diff

        if left == right:
            arr[target] += diff
        if left != right:
            update(left, mid, target, idx*2, diff)
            update(mid + 1, right, target, idx*2 + 1, diff)


init(1, len(arr)-1, 1)
print(segment_tree)
print(query(1, len(arr) - 1, 2, 10, 1))

# 5번 index의 값을 10 으로 변경해라
update(1, len(arr) - 1, 5, 1, 10 - arr[5])
print(query(1, len(arr) -1, 1, 10, 1))