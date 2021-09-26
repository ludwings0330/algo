# title: 구간 곱 구하기
# tag : 세그먼트 트리
import sys
input = lambda: sys.stdin.readline().rstrip()

DIV = 1000000007
def init(node, start, end):
    if start == end:
        Tree[node] = numbers[start]
        return

    init(node*2, start, (start+end)//2)
    init(node*2+1, (start+end)//2+1, end)

    Tree[node] = (Tree[node*2] * Tree[node*2+1])%DIV

def update(node, start, end, idx, num):
    if start > idx or end < idx:
        return


    if start != end:
        update(node*2, start, (start+end)//2, idx, num)
        update(node*2 +1, (start+end)//2+1, end, idx, num)
    else:
        Tree[node] = num
        numbers[idx] = num
        return

    Tree[node] = (Tree[node*2] * Tree[node*2+1])%DIV

def query(node, start, end, query_start, query_end):
    if query_start <= start and end <= query_end:
        return Tree[node]
    if query_start > end or query_end < start:
        return 1

    return (query(node*2, start, (start+end)//2, query_start, query_end) * query(node*2+1, (start+end)//2 +1, end, query_start, query_end))%DIV
N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
Tree = [1] * (2**21)
C = M + K

init(1, 0, N - 1)
while C:
    C -= 1
    a, b, c = map(int, input().split())
    if a == 1:
        # 1 인 경우 b 번째 수를 c 로 바꾼다
        b -= 1
        update(1, 0, N-1, b, c)
        numbers[b] = c

    elif a == 2:
        # 2 인 경우 b부터 c 까지의 곱을 구한다.
        if b > c:
            b, c = c, b
        print(query(1, 0, N-1, b-1, c-1))