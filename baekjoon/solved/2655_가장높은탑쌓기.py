'''
5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2
넓이, 높이, 무게

3
5
3
1
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
bricks = [list(map(int, input().split()))+[i+1] for i in range(N)]

bricks.sort(key=lambda x:(x[0], x[2]), reverse = True)

cache = [-1] * N

'''
tower(n, w) -> 현재위치 n번째, 바로 전 무게가 w 일때 만들 수 있는 최대 높이.
1. 넓이와 무게로 우선 정렬
2. 다음 벽돌의 무게가 더 가벼우면
    1) 탑을 쌓는다.
    2) 쌓지 않고 다음으로 넘어간다.
3. 다음 벽돌의 무게가 더 무거우면 -> 탑을 쌓을 수 없다
    1) 쌓지않고 그 다음 벽돌로넘어가거나
    2) 다음 벽돌부터 재시작
'''
stack = []
def tower(n):
    # n 번째 벽돌이 가장 아래에 있는 벽돌 일때, 만들 수 있는 최대 높이.
    if cache[n] != -1:
        return cache[n]

    cache[n] = bricks[n][1] # n번째 블록이 가장 아래에 있는 벽돌 일때이므로, 최소 h를 쌓아줌

    for i in range(n+1, N):
        # 다음 벽돌이 더 가벼우면 올릴 수 있음.
        if bricks[n][2] > bricks[i][2]:
            # 올리는 방법 중 최대값을 cache에 저장
            cache[n] = max(cache[n], tower(i) + bricks[n][1])


    return cache[n]

for i in range(N):
    tower(i)

MAX = max(cache)
ans = []
for i in range(N):
    if not ans:
        if cache[i] == MAX:
            tmp = bricks[i]
            ans.append(tmp[3])
    else:
        if cache[i] == MAX - tmp[1]:
            MAX -= tmp[1]
            tmp = bricks[i]
            ans.append(tmp[3])
print(len(ans))

for i in range(len(ans)-1, -1, -1):
    print(ans[i])