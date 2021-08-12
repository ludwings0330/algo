# title ; 구간합 구하기
# tag ; segment tree
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
nums_length = len(nums) - 1
Tree = [0] * (2**21)

def init(node, start, end):
    if start == end:
        Tree[node] = nums[start]
        return

    init(node*2, start, (start+end)//2)
    init(node*2+1, (start+end)//2+1, end)

    Tree[node] = Tree[node*2] + Tree[node*2+1]

def update(node, start, end, idx, value):
    if start > idx or end < idx:
        return

    Tree[node] += value

    if start != end:
        update(node*2, start, (start+end)//2, idx, value)
        update(node*2+1, (start+end)//2+1, end, idx, value)

def query(node, start, end, query_start, query_end):
    if query_start <= start and end <= query_end:
        return Tree[node]

    if query_start > end or query_end < start:
        return 0

    return query(node*2, start, (start+end)//2, query_start, query_end) + query(node*2+1, (start+end)//2 +1, end, query_start, query_end)

init(1, 0, nums_length)

for _ in range(M+K):
    M -= 1
    a, b, c = map(int, input().split())

    if a == 1:
        # b 번째 수를 c로 변경
        update(1, 0, nums_length, b-1, c-nums[b-1])
        nums[b-1] = c
    else:
        # b에서 c번째 수의 합 출력
        ret = query(1, 0, nums_length, b-1, c-1)
        print(ret)