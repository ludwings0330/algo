import sys
input = lambda: sys.stdin.readline().rstrip()

N, L = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

board = [line[:] for line in origin_board]
# 가로 길 확인
for r in range(N):
    flag = True
    c = 1
    while c < N:
        k = int(board[r][c-1]) - int(board[r][c])
        if abs(k) > 1:
            flag = False
            break
        # 앞에거보다 지금이 더 낮음
        elif k == 1:
            cnt = 0
            h = board[r][c]
            tmp_c = c
            while cnt < L and tmp_c < N and board[r][tmp_c] == h and board[r][tmp_c] == int(board[r][tmp_c]):
                board[r][tmp_c] += 0.5
                tmp_c += 1
                cnt += 1
            if cnt < L:
                flag = False
                break
        # 뒤가 더 높을때
        elif k == -1:
            cnt = 0
            h = board[r][c-1]
            tmp_c = c-1
            while cnt < L and tmp_c >= 0 and board[r][tmp_c] == h and board[r][tmp_c] == int(board[r][tmp_c]):
                board[r][tmp_c] += 0.5
                tmp_c -= 1
                cnt += 1
            if cnt < L:
                flag = False
                break
        c += 1
    if flag: ans += 1

# 세로 길 확인
for c in range(N):
    flag = True
    r = 1
    while r < N:
        k = int(origin_board[r - 1][c]) - int(origin_board[r][c])
        if abs(k) > 1:
            flag = False
            break
        # 지금이 더 작음
        elif k == 1:
            cnt = 0
            h = origin_board[r][c]
            tmp_r = r
            while cnt < L and tmp_r < N and origin_board[tmp_r][c] == h and origin_board[tmp_r][c] == int(origin_board[tmp_r][c]):
                origin_board[tmp_r][c] += 0.5
                tmp_r += 1
                cnt += 1
            if cnt < L:
                flag = False
                break
        # 뒤가 더 높을때
        elif k == -1:
            cnt = 0
            h = origin_board[r-1][c]
            tmp_r = r-1
            while cnt < L and tmp_r >= 0 and origin_board[tmp_r][c] == h and origin_board[tmp_r][c] == int(origin_board[tmp_r][c]):
                origin_board[tmp_r][c] += 0.5
                tmp_r -= 1
                cnt += 1
            if cnt < L:
                flag = False
                break
        r += 1
    if flag: ans += 1

print(ans)