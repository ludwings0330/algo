# title ; 수열과 쿼리 16
# tag ; 세그먼트 트리
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
Tree = [0] * (2**18)
def init(node, start, end):
    if start == end:
        Tree[node] = (numbers[end], end)
        return

    init(node*2, start, (start + end)//2)
    init(node*2 + 1, (start+end)//2 + 1, end)

    MIN = Tree[node*2][0]
    idx = Tree[node*2][1]
    if MIN > Tree[node*2+1][0]:
        MIN = Tree[node*2+1][0]
        idx = Tree[node*2+1][1]
    Tree[node] = (MIN, idx)

def update(node, start, end, idx, v):
    if idx < start or end < idx:
        return

    if start == end:
        Tree[node] = (numbers[start], start)
        return

    update(node*2, start, (start+end)//2, idx, v)
    update(node*2+1, (start+end)//2 +1, end, idx, v)

    MIN = Tree[node * 2][0]
    idx2 = Tree[node * 2][1]
    if MIN > Tree[node * 2 + 1][0]:
        MIN = Tree[node * 2 + 1][0]
        idx2 = Tree[node * 2 + 1][1]

    Tree[node] = (MIN, idx2)


def query(node, start, end, query_start, query_end):
    if query_end < start or end < query_start:
        return (sys.maxsize, -1)

    if start >= query_start and query_end >= end:
        return Tree[node]

    ret1 = query(node*2, start, (start+end)//2, query_start, query_end)
    ret2 = query(node*2+1, (start+end)//2 + 1, end, query_start, query_end)

    if ret1[0] > ret2[0]:
        return ret2
    else:
        return ret1

init(1, 0, N-1)
while M:
    M -= 1
    a, b, c = map(int, input().split())
    if a == 1:
        # b 인덱스를 c로 바꾼다
        numbers[b-1] = c
        update(1, 0, N-1, b-1, c)
    elif a == 2:
        # b ~ c 중에 최소값을 뽑는다
        if b > c:
            b, c = c, b
        print(query(1, 0, N-1, b-1, c-1)[1] + 1)