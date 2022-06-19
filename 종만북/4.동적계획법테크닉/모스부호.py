import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
my_skip = int(input())
bino = [[0] * 201 for _ in range(201)]

def cal_bino():
    for i in range(201):
        bino[i][0] = bino[i][i] = 1
        for j in range(1,  i):
            bino[i][j] = min(1000000100, bino[i-1][j-1] + bino[i-1][j])



def generate(n, m, s):
    global my_skip

    if my_skip < 0:
        return
    if n == 0 and m == 0:
        if my_skip == 0:
            print(s)
        my_skip -= 1
        return

    if bino[n+m][n] <= my_skip:
        my_skip -= bino[n + m][n]
        return

    if n > 0:
        generate(n-1, m, s + "-")
    if m > 0:
        generate(n, m-1, s + "o")

cal_bino()
generate(n, m, "")
