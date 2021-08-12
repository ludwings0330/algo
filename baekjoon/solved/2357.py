# title ; 최솟값과 최댓값
# tag ; segment tree
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]
nums_length = len(nums) - 1
Tree = [0] * (2**18)

def init(node, start, end):
    # init Tree
    if start == end:
        Tree[node] = [nums[start], nums[start]]
        return

    init(node*2, start, (start+end)//2)
    init(node*2+1, (start+end)//2+1, end)

    MIN = min(Tree[node*2][0], Tree[node*2+1][0])
    MAX = max(Tree[node*2][1], Tree[node*2+1][1])

    Tree[node] = [MIN, MAX]
INF = float('inf')
def query(node, start, end, query_start, query_end):
    # find MIN MAX in range query_start, query_end
    if query_end < start or query_start > end:
        return [INF, -INF] # [MIN, MAX]
    if query_start <= start and end <= query_end:
        return Tree[node]

    left_MIN, left_MAX = query(node*2, start, (start+end)//2, query_start, query_end)
    right_MIN, right_MAX = query(node*2+1, (start+end)//2+1, end, query_start, query_end)

    MIN = min(left_MIN, right_MIN)
    MAX = max(left_MAX, right_MAX)

    return [MIN, MAX]

init(1, 0, nums_length)

while M:
    M-= 1

    a, b = map(int , input().split())
    if a > b:
        a, b = b, a

    print(*query(1, 0, nums_length, a-1, b-1))
