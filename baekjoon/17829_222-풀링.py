import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def solution(sx, ex, sy, ey):
    if ex-sx == 2 and ey-sy == 2:
        nums = []
        for r in range(sy, ey):
            for c in range(sx, ex):
                nums.append(board[r][c])
        return sorted(nums)[-2]

    nums = [solution(sx, (sx+ex)//2, sy, (sy+ey)//2),
            solution((sx+ex)//2, ex, sy, (sy+ey)//2),
            solution(sx, (sx+ex)//2, (sy+ey)//2, ey),
            solution((sx+ex)//2, ex, (sy+ey)//2, ey)]

    return sorted(nums)[-2]


print(solution(0, N, 0, N))

