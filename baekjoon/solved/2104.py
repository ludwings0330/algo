import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
i = 0
tmp = N
size = 0

while tmp > 0:
    tmp = tmp >> 1
    size += 1
size += 1
segment_tree = [0] * (1 << size)
min_tree = [0] * (1 << size)

nums = [0] + list(map(int, input().split()))

def init(left, right, idx):
    if left == right:
        return nums[left]

    mid = (left+right)//2

    segment_tree[idx*2] = init(left, mid, idx*2)
    segment_tree[idx*2 + 1] = init(mid+1, right, idx*2 + 1)
    segment_tree[idx] = segment_tree[idx*2] + segment_tree[idx*2+1]

init(0, N-1, 1)

print(segment_tree)