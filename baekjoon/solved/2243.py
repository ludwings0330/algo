# title ; 사탕상자
# tag ; 세그먼트 트리

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
MAX_SIZE = 2**20
Tree = [0] * (MAX_SIZE*4)

def update(node, start, end, idx, value):
    if idx < start or end < idx:
        return

    Tree[node] += value
    if start == end:
        return
    mid = (start+end)//2

    update(node*2, start, mid, idx, value)
    update(node*2+1, mid+1, end, idx, value)

def query(node, start, end, target): # 순위가 idx 번인걸 꺼내온다
    if start == end:
        print(start)
        update(1, 0, MAX_SIZE, start, -1)
        return start

    mid = (start + end)//2

    if Tree[node*2] >= target:
        return query(node*2, start, mid, target)
    else:
        return query(node*2 +1, mid+1, end, target - Tree[node*2])

while n:
    n -= 1

    command = list(map(int, input().split()))
    A, B = command[0], command[1]

    if A == 1:
        # 사탕상자에서 사탕을 꺼낸다
        # B 는 꺼낼 사탕의 순위를 의미
        query(1, 1, MAX_SIZE, B)

    elif A == 2:
        # 사탕을 넣는 경우
        # B는 넣을 사탕의 맛을 나타내는 정수
        # C는 그러한 사탕의 갯수
        # C가 양수일 경우에는 사탕을 넣고
        # C가 음수일 경우에는 뺀다.
        C = command[2]
        update(1, 1, MAX_SIZE, B, C)

