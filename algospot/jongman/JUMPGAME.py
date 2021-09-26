n = int(input())
def solve(x, y):
    # 기저 사례
    if x >= n or y >= n:
        return 0
    if y == n-1 and x == n-1:
        return 1
    # 메모제이션
    ret = cache[y][x]
    if ret != -1:
        return ret
    jump_size = board[y][x]

    cache[y][x] = (solve(x, y + jump_size)) | solve(x + jump_size, y)
    return cache[y][x]